import os
import requests
from django.core.management.base import BaseCommand
from django.utils import timezone
from dashboard.models import Alert
from dotenv import load_dotenv

load_dotenv()


class Command(BaseCommand):
    help = "Fetch top malicious IPs from AbuseIPDB and create alerts with geolocation data"

    def handle(self, *args, **options):
        url = "https://api.abuseipdb.com/api/v2/blacklist"
        headers = {
            "Key": os.getenv("ABUSEIPDB_KEY", "91b6e11a3437a8f8f9d21e42cf7c366129e9f45d5221d8edc6c52f40555747b3d46bc569bd1e7046"),
            "Accept": "application/json",
        }
        params = {"confidenceMinimum": 90, "limit": 10}

        try:
            response = requests.get(url, headers=headers, params=params, timeout=10)

            if response.status_code == 200:
                data = response.json().get("data", [])
            elif response.status_code == 429:
                # AbuseIPDB daily limit hit — fallback
                self.stdout.write(self.style.WARNING("Rate limit hit – using fallback sample IPs."))
                data = [
                    {"ipAddress": "45.33.32.156", "abuseConfidenceScore": 98, "countryCode": "US"},
                    {"ipAddress": "139.162.123.6", "abuseConfidenceScore": 97, "countryCode": "JP"},
                    {"ipAddress": "185.199.110.153", "abuseConfidenceScore": 95, "countryCode": "DE"},
                ]
            else:
                self.stdout.write(self.style.ERROR(f"API Error: {response.status_code}"))
                return

            count = 0
            for item in data:
                ip = item["ipAddress"]
                score = item["abuseConfidenceScore"]
                country = item.get("countryCode", "Unknown")

                # Skip duplicates
                if Alert.objects.filter(source_ip=ip).exists():
                    continue

                # ---- GEOLOCATION (ip-api.com free, no key needed) ----
                lat = lon = city = country_name = None
                try:
                    geo_resp = requests.get(f"http://ip-api.com/json/{ip}?fields=status,country,city,lat,lon", timeout=5)
                    if geo_resp.status_code == 200:
                        g = geo_resp.json()
                        if g.get("status") == "success":
                            lat = g.get("lat")
                            lon = g.get("lon")
                            city = g.get("city")
                            country_name = g.get("country")
                except Exception as e:
                    print(f"Geo lookup failed for {ip}: {e}")

                # ---- CREATE ALERT ----
                Alert.objects.create(
                    title=f"BLACKLISTED IP: {ip}",
                    description=f"Confidence: {score}% | Country: {country}",
                    severity=self.get_severity(score),
                    source_ip=ip,
                    reported_by="AbuseIPDB Blacklist",
                    date_reported=timezone.now(),
                    latitude=lat,
                    longitude=lon,
                    city=city,
                    country=country_name or country,
                )
                count += 1

            self.stdout.write(self.style.SUCCESS(f"{count} new BLACKLIST alerts created."))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Request failed: {str(e)}"))


    def get_severity(self, score):
        if score >= 98:
            return "Critical"
        elif score >= 95:
            return "High"
        else:
            return "Medium"

