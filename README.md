# 🛡️ CyberDefender  
### _A Security Operations Dashboard for Modern Threat Monitoring_  

CyberDefender is a lightweight **Security Operations Center (SOC)** dashboard built with **Django**, designed to simulate real-world cybersecurity monitoring and alert handling.  
It demonstrates how security analysts can visualize network events, manage incident data, and deploy to the cloud — making it a perfect project for cybersecurity portfolios.  

---

## 🚀 Features  

- 📊 **Threat & Event Visualization** – Interactive dashboards for network logs or simulated attack data  
- ⚙️ **Modular Django Apps** – Organized structure for easy feature expansion  
- ☁️ **Cloud Deployment** – Fully deployed on [Heroku](https://www.heroku.com/)  
- 🧠 **Database Integration** – Uses PostgreSQL (Heroku) or SQLite (local)  
- 🔐 **Cybersecurity Focused** – Great example for SOC, DevSecOps, or Cloud Security roles  

---

## 🧩 Tech Stack  

| Category | Technologies |
|-----------|---------------|
| **Backend** | Python 🐍, Django 🕸️ |
| **Database** | PostgreSQL (Production), SQLite (Local) |
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

