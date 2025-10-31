from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import SecurityAlert
from django.utils import timezone
import requests

def home(request):
    return render(request, 'dashboard/home.html')

@login_required
def alerts(request):
    alerts_list = SecurityAlert.objects.all().order_by('-date_reported')
    context = {
        'alerts': alerts_list,
        'critical': SecurityAlert.objects.filter(severity='Critical').count(),
        'high': SecurityAlert.objects.filter(severity='High').count(),
        'medium': SecurityAlert.objects.filter(severity='Medium').count(),
        'low': SecurityAlert.objects.filter(severity='Low').count(),
    }
    return render(request, 'dashboard/alerts.html', context)

@login_required
def add_alert(request):
    if request.method == 'POST':
        alert = SecurityAlert(
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

@login_required
def check_ip(request):
    result = None
    if request.method == 'POST':
        ip = request.POST['ip']
        url = "https://api.abuseipdb.com/api/v2/check"
        headers = {
            'Key': '91b6e11a3437a8f8f9d21e42cf7c366129e9f45d5221d8edc6c52f40555747b3d46bc569bd1e7046',  # ← FIX THIS
            'Accept': 'application/json',
        }
        params = {
            'ipAddress': ip,
            'maxAgeInDays': 90
        }

        try:
            response = requests.get(url, headers=headers, params=params)
            if response.status_code == 200:
                data = response.json()['data']
                result = {
                    'ip': ip,
                    'score': data['abuseConfidenceScore'],
                    'country': data.get('countryCode', 'Unknown'),
                    'reports': data['totalReports'],
                    'isp': data.get('isp', 'Unknown'),
                    'is_malicious': data['abuseConfidenceScore'] >= 75
                }
            else:
                result = {'error': f"API Error: {response.status_code}"}
        except Exception as e:
            result = {'error': f"Request failed: {str(e)}"}

    return render(request, 'dashboard/check_ip.html', {'result': result})
