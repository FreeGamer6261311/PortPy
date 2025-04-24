# 🔍 PortPy – Lightweight Python Port Scanner

PortPy is a simple and effective command-line port scanner written in Python.  
It allows users to scan the first 1024 TCP ports of any IP address or domain name.

---

## ✨ Features

- ✅ Accepts both IP addresses and domain names
- 🌐 Automatically resolves domains to IP addresses (fallback with `nslookup`)
- ⚡ Scans ports from 1 to 1024 with timeout control
- 🔓 Displays open ports clearly
- 🖼️ ASCII banner for style

---

## 📦 Installation

Clone the repository and navigate into it:

git clone https://github.com/your-username/portpy.git
cd portpy

! Make sure you have Python 3 installed:

python3 --version

🚀 Usage

-Scan an IP-
python3 portpy.py 192.168.1.1

-Scan a domain:-
python3 portpy.py example.com

The scanner will:
Resolve the domain (if needed)
Scan ports 1–1024
List any open ports

🧠 Example Output


  .------..------..------..------..------..------..------..------.
  |P.--. ||O.--. ||R.--. ||T.--. ||P.--. ||Y.--. ||  #   ||  #   |
  '------''------''------''------''------''------''------''------'

                  Simple Port Scanner by PortPy
  
  [*] Starting scan on: 45.33.32.156
  
  [+] Port 21 is open
  [+] Port 80 is open
  [+] Port 443 is open
  
  [*] Scan complete.


⚠️ Legal Disclaimer
This tool is for educational and authorized penetration testing only.
Do not scan any system without explicit permission. Unauthorized scanning is illegal.

👨‍💻 Author
Developed by [FreeGamer_]
Feel free to fork, star ⭐, and contribute!
