# FCaG

IP Information Fetcher

Author: LocalHost.07

Description

This Bash script allows you to fetch detailed information about any public IP address.

It retrieves data such as IP address, hostname, location (city, region, country), organization, and more from ipinfo.io. Additionally, it fetches ASN and continent information using the ipgeolocation.io API for enhanced geolocation data.

Features

Custom Banner: A styled banner is displayed at the start.

Loading Animation: A spinner animation to simulate loading while fetching data.

IP Information: Retrieves and displays:

• IP address
• Hostname
• City
• Region
• CountryLocation 
• coordinates (latitude, longitude)
• Organization
• Postal code
• TimezoneASN (Autonomous System Number)
• Continent name

Validation: The script checks if the input is a valid IPv4 address.

PrerequisitesBash: Ensure you're running this script in a Unix-based shell (e.g., Linux, macOS, or Termux on Android).

jq: A lightweight command-line JSON processor is required to parse the API responses.To install jq, run:sudo apt install jqAPI Key: To retrieve ASN and continent information, you will need an API key from ipgeolocation.io.Sign up for an API key at: https://ipgeolocation.io/signupReplace YOUR_API_KEY in the script with your actual API key.UsageClone or download the script:git clone <repository-link>
cd <repository-folder>Run the script:bash main.shInput an IP address when prompted:Please enter the IP address > 8.8.8.8View the results: The script will display the IP details, including ASN and continent information.Example OutputPlease enter the IP address > 8.8.8.8
[*] Fetching details for IP: 8.8.8.8...

------------------- IP Information -------------------
IP: 8.8.8.8
Hostname: dns.google
City: Mountain View
Region: California
Country: US
Location: 37.3860,-122.0838
Organization: AS15169 Google LLC
Postal: 94043
Timezone: America/Los_Angeles
ASN: AS15169
Continent: North America
------------------------------------------------------Error HandlingIf the IP address format is invalid, the script will display an error:[!] Invalid IP format! Please enter a valid IP.If the jq tool is missing, the script will prompt you to install it:[!] jq is not installed. Install it with 'sudo apt install jq'.API Rate LimitsThe API services (ipinfo.io and ipgeolocation.io) have free-tier limits. Ensure you manage the requests appropriately or consider upgrading the plan if needed for large-scale usage.LicenseThis script is free to use and modify. Attribution to the original author (LocalHost.07) is appreciated if redistributed.
