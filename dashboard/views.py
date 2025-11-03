from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
import requests
from .models import Alert


# HOME + IP SCANNER (ALL IN ONE)
def home(request):
    result = None
    if request.method == 'POST' and 'ip' in request.POST:
        ip = request.POST['ip'].strip()

        # LOCALHOST
        if ip in ['127.0.0.1', 'localhost', '::1']:
            result = {
                'ip': ip, 'score': 0, 'country': 'Local', 'reports': 0,
                'isp': 'Your Machine', 'is_malicious': False,
                'vt_detections': 0, 'shodan_ports': 'N/A'
            }
        else:
            # ABUSEIPDB
            abuse_url = "https://api.abuseipdb.com/api/v2/check"
            abuse_headers = {
                'Key': '91b6e11a3437a8f8f9d21e42cf7c366129e9f45d5221d8edc6c52f40555747b3d46bc569bd1e7046',
                'Accept': 'application/json',
            }
            try:
                r = requests.get(abuse_url, headers=abuse_headers, params={'ipAddress': ip, 'maxAgeInDays': 90}, timeout=10)
                if r.status_code == 200:
                    d = r.json()['data']
                    result = {
                        'ip': ip,
                        'score': d['abuseConfidenceScore'],
                        'country': d.get('countryCode', '??'),
                        'reports': d['totalReports'],
                        'isp': d.get('isp', 'Unknown'),
                        'is_malicious': d['abuseConfidenceScore'] >= 75,
                        'vt_detections': 0,
                        'shodan_ports': 'N/A'
                    }
                else:
                    result = {'error': f"AbuseIPDB: {r.status_code}"}
            except:
                result = {'error': 'AbuseIPDB failed'}

            # VIRUSTOTAL (FREE KEY)
            if not result.get('error'):
                try:
                    vt_url = "https://www.virustotal.com/vtapi/v2/ip-address/report"
                    vt_params = {'apikey': '2dbe5f191a010332ddf445e3e68887515ae9758e1fb085ab8a1bb28cea8f6e67', 'ip': ip}  # ← GET FREE
                    r = requests.get(vt_url, params=vt_params, timeout=10)
                    if r.status_code == 200:
                        data = r.json()
                        result['vt_detections'] = len(data.get('detected_urls', []))
                except:
                    result['vt_detections'] = 'Error'

            # SHODAN (FREE KEY)
            if not result.get('error'):
                try:
                    shodan_url = f"https://api.shodan.io/shodan/host/{ip}"
                    shodan_params = {'key': 'g1WBODYCnEd2FF1g2BaLRb4ltb76DtiL'}  # ← GET FREE
                    r = requests.get(shodan_url, params=shodan_params, timeout=10)
                    if r.status_code == 200:
                        data = r.json()
                        ports = ', '.join(map(str, data.get('ports', []))) or 'None'
                        result['shodan_ports'] = ports
                        result['shodan_os'] = data.get('os', 'Unknown')
                except:
                    result['shodan_ports'] = 'Error'

    return render(request, 'dashboard/home.html', {'result': result})

# ALERTS LIST + CHART
@login_required
def alerts(request):
    alerts_list = Alert.objects.all().order_by('-date_reported')
    context = {
        'alerts': alerts_list,
        'critical': Alert.objects.filter(severity='Critical').count(),
        'high': Alert.objects.filter(severity='High').count(),
        'medium': Alert.objects.filter(severity='Medium').count(),
        'low': Alert.objects.filter(severity='Low').count(),
    }
    return render(request, 'dashboard/alerts.html', context)

# REGISTER
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'dashboard/register.html', {'form': form})

# ADD ALERT (REPORT INCIDENT)
@login_required
def add_alert(request):
    if request.method == 'POST':
        alert = Alert(
            title=request.POST['title'],
            description=request.POST['description'],
            severity=request.POST['severity'],
            source_ip=request.POST.get('source_ip') or None,
            reported_by=request.POST.get('reported_by', request.user.username),
            date_reported=timezone.now()
        )
        alert.save()
        return redirect('alerts')
    return render(request, 'dashboard/add_alert.html')

# DELETE ALERT (ADMIN ONLY)
@login_required
def delete_alert(request, alert_id):
    if request.user.is_superuser:
        Alert.objects.filter(id=alert_id).delete()
    return redirect('alerts')
