# 🛡️ CyberDefender  
A Security Operations Dashboard for Modern Threat Monitoring  

**CyberDefender** is a lightweight Security Operations Center (SOC) dashboard built with Django, designed to simulate real-world cybersecurity monitoring and alert handling.  
It demonstrates how security analysts can visualize network events, manage incident data, and deploy to the cloud — making it a perfect project for cybersecurity portfolios.  

---

## 🚀 Features  
- 📊 **Threat & Event Visualization** – Interactive global map with live attack pins  
- 🌍 **Global Threat Map** – Displays real-time geolocation of simulated or API-based alerts  
- 🔍 **Shodan & VirusTotal Integration** – Enriches alerts with IP intelligence and file reputation data  
- ⚙️ **Modular Django Apps** – Clean structure for extending new features  
- ☁️ **Cloud Deployment** – Fully deployed on **Heroku**  
- 🧠 **Database Integration** – Uses PostgreSQL (Heroku) or SQLite (local)  
- 🔐 **Cybersecurity Focused** – Ideal for SOC, DevSecOps, or Cloud Security demonstrations  

---

## 🧩 Tech Stack  

| Category | Technologies |
|-----------|---------------|
| **Backend** | Python 🐍, Django 🕸️ |
| **Database** | PostgreSQL (Production), SQLite (Local) |
| **Deployment** | Heroku ☁️ |
| **Version Control** | Git & GitHub |
| **Other Tools** | Shodan API, VirusTotal API, Gunicorn, dj-database-url, Whitenoise |

---

## 🧱 Local Development  

```bash
# Clone the repository
git clone https://github.com/abhaysam04/cyberdefender.git
cd cyberdefender

# Create virtual environment
python3 -m venv venv
source venv/bin/activate   # (Mac/Linux)
venv\Scripts\activate      # (Windows)

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the development server
python manage.py runserver
🧭 Running the Feed Alerts Script
bash
Copy code
python manage.py feed_alerts
This script pulls simulated or API-based threat data (Shodan, VirusTotal, etc.) and populates alerts into the dashboard with geolocation.

☁️ Deployment
Deployed on Heroku with automated builds and PostgreSQL database configuration via dj-database-url.
A Heroku Scheduler Add-on runs the feed_alerts command periodically to simulate continuous threat monitoring.

📡 Live Demo
🔗 Deployed App: https://cyberdefender-abhay.herokuapp.com
💻 Source Code: https://github.com/abhaysam04/cyberdefender

🔑 Demo Login
Use these demo credentials to explore the dashboard:

makefile
Copy code
Username: admin  
Password: cyber2025!
⚠️ Note: These credentials are for demo purposes only and do not provide access to any real data or systems.

🧑‍💻 Author
Abhay Samdhyan
Cybersecurity Student | SOC & Cloud Security Enthusiast

📧 Email: abhaysamdhyan04@gmail.com
🌐 LinkedIn | GitHub
