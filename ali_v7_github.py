#!/usr/bin/env python3
# ALI TOOLS V7 - GITHUB EDITION
# Author: Sami | Karachi, Pakistan
# GitHub: github.com/sami

import socket, random, string, requests, os, time, datetime
from colorama import Fore, Style, init
init(autoreset=True)

VERSION = "V7 GitHub Edition"

def banner():
    os.system("clear")
    print(Fore.CYAN + Style.BRIGHT + f"""
    █████╗ ██╗ ██╗ ██████╗ ██╗ ██╗ ██████╗
    ██╔══██╗██║ ██║ ██╔═══██╗██║ ██║██╔════╝
    ███████║██║ ██║ ██║ ██║██║ ██║███████╗
    ██╔══██║██║ ██║ ██║ ██║██║ ██║██╔═══██╗
    ██║ ██║███████╗██║ ╚██████╔╝╚██████╔╝╚██████╔╝
    ╚═╝ ╚═╝╚══════╝╚═╝ ╚═════╝ ╚═════╝ ╚═════╝
    """ + Fore.YELLOW + f" --- {VERSION} - MADE BY SAMI | KARACHI | 2026 ---\n" + Style.RESET_ALL)

def port_scanner():
    target = input(Fore.GREEN + "Target IP/Domain: " + Style.RESET_ALL).strip()
    if not target:
        print(Fore.RED + "[X] Target likho!" + Style.RESET_ALL)
        return
    print(Fore.YELLOW + f"\n[~] Scanning {target}...\n" + Style.RESET_ALL)
    try:
        ip = socket.gethostbyname(target)
        print(f"Resolved IP: {ip}\n")
        common_ports = {21:"FTP",22:"SSH",23:"Telnet",25:"SMTP",53:"DNS",80:"HTTP",110:"POP3",443:"HTTPS",3306:"MySQL",8080:"HTTP-Proxy"}
        open_found = []
        for port, service in common_ports.items():
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1.5)
            result = s.connect_ex((ip, port))
            if result == 0:
                print(Fore.GREEN + f"[OPEN] Port {port} - {service}" + Style.RESET_ALL)
                open_found.append(port)
            else:
                print(Fore.RED + f"[CLOSE] Port {port}" + Style.RESET_ALL)
            s.close()

        # Save log
        with open("scan_log.txt", "a") as f:
            f.write(f"\n[{datetime.datetime.now()}] {target} ({ip}) -> OPEN: {open_found}\n")
        print(Fore.CYAN + f"\n[✓] {len(open_found)} open ports found. Saved to scan_log.txt" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"[X] Error: {e}" + Style.RESET_ALL)

def password_gen():
    try:
        length = int(input("Length (16): ") or "16")
        count = int(input("Kitne? (10): ") or "10")
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
        print(Fore.CYAN + "\nGenerating...\n" + Style.RESET_ALL)
        with open("passwords.txt", "a") as f:
            f.write(f"\n--- {now} | V7 ---\n")
            for i in range(count):
                pwd = "".join(random.choice(chars) for _ in range(length))
                print(f"{i+1}. {pwd}")
                f.write(f"{pwd}\n")
        print(Fore.GREEN + "\n[✓] Saved to passwords.txt" + Style.RESET_ALL)
    except:
        print(Fore.RED + "[X] Number sahi likho!" + Style.RESET_ALL)

def ip_tracker():
    ip = input("IP (empty for own): ").strip()
    url = f"http://ip-api.com/json/{ip}" if ip else "http://ip-api.com/json/"
    try:
        r = requests.get(url, timeout=5).json()
        if r['status'] == 'success':
            print(Fore.GREEN + f"\n[IP] {r['query']}" + Style.RESET_ALL)
            print(f"[Country] {r['country']} ({r['countryCode']})")
            print(f"[City] {r['city']}, {r['regionName']} {r['zip']}")
            print(f"[ISP] {r['isp']} | {r['org']}")
            print(f"[Timezone] {r['timezone']}")
            link = f"https://www.google.com/maps/search/{r['lat']},{r['lon']}"
            print(Fore.CYAN + f"[Map] {link}" + Style.RESET_ALL)
            try:
                os.system(f"termux-open-url {link}")
            except:
                pass
        else:
            print(Fore.RED + "[X] IP nahi mila!" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"[X] {e}" + Style.RESET_ALL)

# Main Loop
while True:
    banner()
    print(Fore.YELLOW + "1. Port Scanner PRO\n2. Password Generator PRO\n3. IP Tracker PRO\n4. View Logs\n5. Exit" + Style.RESET_ALL)
    c = input(Fore.WHITE + Style.BRIGHT + "\nOption (1-5): " + Style.RESET_ALL)
    if c == "1": port_scanner()
    elif c == "2": password_gen()
    elif c == "3": ip_tracker()
    elif c == "4":
        os.system("cat scan_log.txt 2>/dev/null || echo 'No logs yet'; cat passwords.txt 2>/dev/null | tail -20")
    elif c == "5":
        print(Fore.MAGENTA + "\nAllah Hafiz Sami! GitHub pe milte hain! ❤️🇵🇰" + Style.RESET_ALL)
        break
    input(Fore.WHITE + "\nEnter dabao...")
