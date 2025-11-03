# 🛡️ CyberDefender  
### A Security Operations Dashboard for Modern Threat Monitoring  

**CyberDefender** is a lightweight **Security Operations Center (SOC)** dashboard built with **Django**, designed to simulate real-world cybersecurity monitoring and alert handling.  
It demonstrates how security analysts can visualize global threats, analyze indicators using OSINT tools, and manage alerts — making it perfect for portfolios, learning SOC workflows, or demonstrating cybersecurity engineering skills.  

---

## 🚀 Features  

- 📊 **Threat & Event Visualization** – Real-time dashboards for simulated network events and security alerts  
- 🌍 **Global Threat Map** – Displays live attack data and geolocation insights for a visual global overview  
- 🕵️ **Shodan API Integration** – Gathers device and exposure data from the Shodan search engine  
- 🧬 **VirusTotal Lookup** – Checks file hashes and URLs against VirusTotal for threat intelligence enrichment  
- ⚙️ **Modular Django Apps** – Clean and extensible structure for adding new SOC modules  
- ☁️ **Cloud Deployment** – Fully deployed and hosted on **Heroku**  
- 🧠 **Database Integration** – Supports **PostgreSQL** (production) and **SQLite** (local development)  
- 🔐 **Cybersecurity-Focused** – Built for demonstrating SOC, Threat Intelligence, or Cloud Security skills  

---

## 🧩 Tech Stack  

| Category | Technologies |
|-----------|--------------|
| **Backend** | Python 🐍, Django 🕸️ |
| **Database** | PostgreSQL (Production), SQLite (Local) |
| **Threat Intelligence APIs** | Shodan, VirusTotal |
| **Deployment** | Heroku ☁️ |
| **Version Control** | Git & GitHub |
| **Other Tools** | Gunicorn, dj-database-url, Whitenoise |

---

## ⚙️ Setup Instructions  

### 🧱 Local Development  

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
This script pulls simulated or API-based threat data and populates alerts into the dashboard.

☁️ Deployment
Deployed on Heroku with automated builds and database configuration via dj-database-url.
Scheduler add-on runs periodic data ingestion (feed_alerts) for continuous updates.

📡 Live Demo
🔗 Deployed App: https://cyberdefender-abhay.herokuapp.com
💻 Source Code: https://github.com/abhaysam04/cyberdefender

🧑‍💻 Author
Abhay Samdhyan
Cybersecurity Student | SOC & Cloud Security Enthusiast
📧 abhaysamdhyan04@gmail.com
🌐 LinkedIn | GitHub

