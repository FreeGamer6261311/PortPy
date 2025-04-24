import socket
import sys
import os

def print_banner():
    print(r"""
.------..------..------..------..------..------..------..------.
|P.--. ||O.--. ||R.--. ||T.--. ||P.--. ||Y.--. ||  #   ||  #   |
| :/\: || :/\: || :(): || :/\: || :/\: || (\/) ||      ||      |
| (__) || :\/: || ()() || (__) || (__) || :\/: ||      ||      |
| '--'P|| '--'O|| '--'R|| '--'T|| '--'P|| '--'Y||      ||      |
'------''------''------''------''------''------''------''------'
    """)
    print("              Simple Port Scanner by FreeGamer_\n")

def resolve_target(target):
    try:
        socket.inet_aton(target)  # checks if it's a valid IP
        return target
    except socket.error:
        try:
            ip = socket.gethostbyname(target)
            return ip
        except socket.gaierror:
            print(f"[!] Failed to resolve domain: {target}")
            # Optional fallback using nslookup
            print("[*] Trying nslookup...")
            try:
                result = os.popen(f"nslookup {target}").read()
                lines = result.splitlines()
                for line in lines:
                    if "Address" in line and not line.startswith("Server"):
                        ip = line.split()[-1]
                        print(f"[+] Resolved via nslookup: {ip}")
                        return ip
                print("[!] nslookup failed to resolve IP.")
            except Exception as e:
                print(f"[!] nslookup error: {e}")
            return None

def scan_ports(ip):
    print(f"[*] Starting scan on: {ip}\n")
    for port in range(1, 1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((ip, port))
        if result == 0:
            print(f"[+] Port {port} is open")
        s.close()
    print("\n[*] Scan complete.")

if __name__ == "__main__":
    print_banner()

    if len(sys.argv) != 2:
        print("Usage: python portpy.py <target_ip_or_domain>")
        sys.exit(1)

    target = sys.argv[1]
    ip = resolve_target(target)

    if ip:
        scan_ports(ip)
