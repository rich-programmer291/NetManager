# 🌐 NetManager: Network Monitoring Dashboard

![Python](https://img.shields.io/badge/Python-3.x-emerald)
![Django](https://img.shields.io/badge/Framework-Django-092e20)
![TailwindCSS](https://img.shields.io/badge/UI-Tailwind_CSS-38bdf8)

**NetManager** is a lightweight, high-performance network device management system. Built with a "Cyber-Noir" aesthetic, it allows network administrators to track assets, monitor online/offline status, and resolve hostnames through a terminal-inspired interface.

---

## ✨ Key Features

* **⚡ Cyber-Noir Interface:** A unified aesthetic using JetBrains Mono and Inter fonts for a professional "terminal" feel.
* **🌓 Adaptive Theming:** Native Dark/Light mode toggle with persistence (LocalStorage).
* **📊 Network Intelligence:** Real-time dashboard showing counts of Active vs. Disconnected nodes.
* **🔍 IP Lookup Tool:** Integrated hostname resolution with built-in "Copy-to-Clipboard" functionality.
* **📱 Fully Responsive:** Optimized for mobile auditing and desktop monitoring.

---

## 🛠️ Tech Stack

- **Backend:** Django 5.x
- **Frontend:** HTML5, JavaScript (ES6+)
- **Styling:** Tailwind CSS (CDN)
- **Typography:** JetBrains Mono & Inter (Google Fonts)

---

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/rich-programmer291/NetManager.git
cd netmng
```
### 2. Run Locally
- pip install -r requirements.txt
- python manage.py migrate

## Project Structure
```
.
├── netmng/                 # Project Configuration Root
│   ├── __init__.py         # Marks directory as a Python package
│   ├── settings.py         # Global Suite Settings (Security Keys, DB Config)
│   ├── urls.py             # Main Routing Table (The "Switchboard")
│   ├── asgi.py             # Interface for Asynchronous Servers
│   └── wsgi.py             # Interface for Synchronous Web Servers
├── devices/                # Asset Management App (Core Logic)
│   ├── migrations/         # Version control for Database Schema  
│   ├── templates/          # Cyber-Noir UI Layer (HTML/Tailwind)
│   │   ├── base.html       # Global Layout & Dark Mode Logic
│   │   ├── list.html       # Network Dashboard & Status Summary
│   │   └── ...             # Add, Update, and Lookup views
│   ├── admin.py            # Backend Management Portal configuration
│   ├── apps.py             # Application-specific configuration
│   ├── models.py           # Network Schemas (Device, IP, Type definitions)
│   ├── tests.py            # Automated Unit Tests for Network Logic
│   └── views.py            # Intelligence Logic (IP Resolution, CRUD ops)
├── db.sqlite3              # Local Database Instance (Keep out of GitHub)
├── manage.py               # Django Command-Line Utility (Execution Entry)
└── requirements.txt        # Manifest of Python dependencies
```

## Screenshots

![Screenshot_22-3-2026_19277_127 0 0 1](https://github.com/user-attachments/assets/7cb51f30-c04c-4328-bff5-a74f609851d3)
 <br/>
![Screenshot_22-3-2026_192735_127 0 0 1](https://github.com/user-attachments/assets/d55c706f-5773-4f25-971d-9dec9e80e541)


