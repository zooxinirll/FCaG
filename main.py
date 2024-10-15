import os
import sys
import time
import requests

# Colors for terminal output
BLUE = "\033[1;34m"
MAGENTA = "\033[1;35m"
CYAN = "\033[1;36m"
GREEN = "\033[1;32m"
RED = "\033[1;31m"
YELLOW = "\033[1;33m"
RESET = "\033[0m"


def banner():
    print(f"{MAGENTA}")
    print(" ███████╗ ██████╗ █████╗  ██████╗ ")
    print(" ██╔════╝██╔════╝██╔══██╗██╔════╝ ")
    print(" █████╗  ██║     ███████║██║  ███╗")
    print(" ██╔══╝  ██║     ██╔══██║██║   ██║")
    print(" ██║     ╚██████╗██║  ██║╚██████╔╝")
    print(" ╚═╝      ╚═════╝╚═╝  ╚═╝ ╚═════╝ ")
    print("                                  ")
    print(f"{CYAN}           Author: LocalHost.07{RESET}")
    print("")


def spinner():
    spinstr = "⠋⠙⠸⠴⠦⠇"
    while True:
        for char in spinstr:
            sys.stdout.write(f" [{char}]  ")
            sys.stdout.flush()
            time.sleep(0.1)
            sys.stdout.write("\b\b\b\b\b\b\b")


def fetch_ip_details(ip):
    print(f"{GREEN}[*] Fetching details for IP: {ip}...{RESET}")
    
    # Fetching IP data from ipinfo.io
    try:
        response = requests.get(f"http://ipinfo.io/{ip}/json").json()
    except requests.RequestException as e:
        print(f"{RED}[!] Error fetching data: {e}{RESET}")
        sys.exit(1)

    # Simulate loading with spinner
    time.sleep(1)

    if "bogon" in response:
        print(f"{RED}[!] Invalid IP address or error fetching data!{RESET}")
        sys.exit(1)

    print(f"{CYAN}------------------- IP Information -------------------{RESET}")
    print(f"{YELLOW}IP:{RESET} {response.get('ip', 'N/A')}")
    print(f"{YELLOW}Hostname:{RESET} {response.get('hostname', 'N/A')}")
    print(f"{YELLOW}City:{RESET} {response.get('city', 'N/A')}")
    print(f"{YELLOW}Region:{RESET} {response.get('region', 'N/A')}")
    print(f"{YELLOW}Country:{RESET} {response.get('country', 'N/A')}")
    print(f"{YELLOW}Location:{RESET} {response.get('loc', 'N/A')}")
    print(f"{YELLOW}Organization:{RESET} {response.get('org', 'N/A')}")
    print(f"{YELLOW}Postal:{RESET} {response.get('postal', 'N/A')}")
    print(f"{YELLOW}Timezone:{RESET} {response.get('timezone', 'N/A')}")

    # Fetch ASN and continent details with error handling
    try:
        asn_response = requests.get(f"https://api.ipinfo.io/{ip}/asn").json()
        asn = asn_response.get('asn', 'N/A')
    except requests.RequestException as e:
        print(f"{RED}[!] Error fetching ASN data: {e}{RESET}")
        asn = 'N/A'

    try:
        continent_response = requests.get(f"https://api.ipgeolocation.io/ipgeo?apiKey=YOUR_API_KEY&ip={ip}").json()
        continent = continent_response.get('continent_name', 'N/A')
    except requests.RequestException as e:
        print(f"{RED}[!] Error fetching continent data: {e}{RESET}")
        continent = 'N/A'

    print(f"{YELLOW}ASN:{RESET} {asn}")
    print(f"{YELLOW}Continent:{RESET} {continent}")
    print(f"{CYAN}------------------------------------------------------{RESET}")


def validate_ip(ip):
    parts = ip.split(".")
    if len(parts) != 4 or not all(part.isdigit() and 0 <= int(part) <= 255 for part in parts):
        print(f"{RED}[!] Invalid IP format! Please enter a valid IP.{RESET}")
        sys.exit(1)


def main():
    banner()

    ip = input(f"{MAGENTA}Please enter the IP address > {RESET}").strip()

    if not ip:
        print(f"{RED}[!] No IP entered. Exiting...{RESET}")
        sys.exit(1)

    # Validate the IP address format
    validate_ip(ip)
    fetch_ip_details(ip)


if __name__ == "__main__":
    main()
