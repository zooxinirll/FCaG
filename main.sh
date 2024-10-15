#!/bin/bash

# Colors
BLUE="\033[1;34m"
MAGENTA="\033[1;35m"
CYAN="\033[1;36m"
GREEN="\033[1;32m"
RED="\033[1;31m"
YELLOW="\033[1;33m"
RESET="\033[0m"

function banner() {
    echo -e "${MAGENTA}"
    echo " ███████╗ ██████╗ █████╗  ██████╗ ";
    echo " ██╔════╝██╔════╝██╔══██╗██╔════╝ ";
    echo " █████╗  ██║     ███████║██║  ███╗";
    echo " ██╔══╝  ██║     ██╔══██║██║   ██║";
    echo " ██║     ╚██████╗██║  ██║╚██████╔╝";
    echo " ╚═╝      ╚═════╝╚═╝  ╚═╝ ╚═════╝ ";
    echo "                                  ";
    echo -e "${CYAN}           Author: LocalHost.07${RESET}"
    echo ""
}


function spinner() {
    local pid=$!
    local delay=0.1
    local spinstr="⠋⠙⠸⠴⠦⠇"
    echo -n "  "
    while ps -p $pid &> /dev/null; do
        for char in $(echo $spinstr | fold -w1); do
            echo -ne " [$char]  "
            sleep $delay
            echo -ne "\b\b\b\b\b\b\b"
        done
    done
    echo -ne "\b\b\b\b\b\b\b"
}


function fetch_ip_details() {
    local ip=$1
    echo -e "${GREEN}[*] Fetching details for IP: $ip...${RESET}"
    
    # Fetching IP data from ipinfo.io
    response=$(curl -s "http://ipinfo.io/$ip/json")

    # Simulating loading
    sleep 1 & spinner

    # Extracting data
    if echo "$response" | grep -q "Invalid"; then
        echo -e "${RED}[!] Invalid IP address or error fetching data!${RESET}"
        exit 1
    fi

    
    echo -e "${CYAN}------------------- IP Information -------------------${RESET}"
    echo -e "${YELLOW}IP:${RESET} $(echo "$response" | jq -r '.ip')"
    echo -e "${YELLOW}Hostname:${RESET} $(echo "$response" | jq -r '.hostname')"
    echo -e "${YELLOW}City:${RESET} $(echo "$response" | jq -r '.city')"
    echo -e "${YELLOW}Region:${RESET} $(echo "$response" | jq -r '.region')"
    echo -e "${YELLOW}Country:${RESET} $(echo "$response" | jq -r '.country')"
    echo -e "${YELLOW}Location:${RESET} $(echo "$response" | jq -r '.loc')"
    echo -e "${YELLOW}Organization:${RESET} $(echo "$response" | jq -r '.org')"
    echo -e "${YELLOW}Postal:${RESET} $(echo "$response" | jq -r '.postal')"
    echo -e "${YELLOW}Timezone:${RESET} $(echo "$response" | jq -r '.timezone')"
    
    
    asn=$(curl -s "https://api.ipinfo.io/$ip/asn" | jq -r '.asn')
    continent=$(curl -s "https://api.ipgeolocation.io/ipgeo?apiKey=YOUR_API_KEY&ip=$ip" | jq -r '.continent_name')

    echo -e "${YELLOW}ASN:${RESET} ${asn:-N/A}"
    echo -e "${YELLOW}Continent:${RESET} ${continent:-N/A}"
    echo -e "${CYAN}------------------------------------------------------${RESET}"
}


function validate_ip() {
    local ip=$1
    if [[ ! $ip =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
        echo -e "${RED}[!] Invalid IP format! Please enter a valid IP.${RESET}"
        exit 1
    fi
}


banner
echo -ne "${MAGENTA}Please enter the IP address > ${RESET}"
read -r ip

if [[ -z "$ip" ]]; then
    echo -e "${RED}[!] No IP entered. Exiting...${RESET}"
    exit 1
fi

# Ensure jq is installed
if ! command -v jq &> /dev/null; then
    echo -e "${RED}[!] jq is not installed. Install it with 'sudo apt install jq'.${RESET}"
    exit 1
fi

# Validate and fetch IP details
validate_ip "$ip"
fetch_ip_details "$ip"
