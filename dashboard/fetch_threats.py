import requests
from .models import SecurityAlert
from django.utils import timezone

API_KEY = '91b6e11a3437a8f8f9d21e42cf7c366129e9f45d5221d8edc6c52f40555747b3d46bc569bd1e7046'  # ← YOUR KEY
URL = 'https://api.abuseipdb.com/api/v2/blacklist'

def fetch_malicious_ips():
    headers = {
        'Key': API_KEY,
        'Accept': 'application/json',
    }
    params = {
        'confidenceMinimum': 90,
        'limit': 10,
    }

    response = requests.get(URL, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        count = 0
        for item in data['data']:
            ip = item['ipAddress']
            abuse_confidence = item['abuseConfidenceScore']
            country = item.get('countryCode', 'Unknown')
            report_count = item.get('reportCount', 0)

            # Build description — only show report count if > 0
            desc_lines = [
                f"Abuse Confidence: {abuse_confidence}%",
                f"Country: {country}"
            ]
            if report_count > 0:
                desc_lines.append(f"Reported {report_count} times")
            desc_lines.append("Source: AbuseIPDB")
            description = "\n".join(desc_lines)

            SecurityAlert.objects.get_or_create(
                source_ip=ip,
                defaults={
                    'title': f"Malicious IP Detected: {ip}",
                    'description': description,
                    'severity': 'Critical' if abuse_confidence >= 95 else 'High',
                    'reported_by': 'AbuseIPDB Auto-Feed',
                    'date_reported': timezone.now(),
                    'is_verified': True
                }
            )
            count += 1
        print(f"Added {count} malicious IPs!")
    else:
        print(f"Error: {response.status_code} - {response.text}")
