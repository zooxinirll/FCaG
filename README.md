# FCaG - IP Information Fetcher

**Author:** LocalHost.07

## Overview

The FCaG (Fetch Comprehensive and Geolocated IP Information) is an advanced Bash-based tool designed for retrieving detailed information about public IP addresses. This script gathers data from leading services like ipinfo.io and ipgeolocation.io, making it a powerful utility for network administrators, cybersecurity experts, and developers.

FCaG delivers critical information including IP address, hostname, geolocation (city, region, country), organization, ASN (Autonomous System Number), and continent details—all in one consolidated report.

## Features

- **Custom Banner:** Start the script with a personalized, visually appealing banner.
- **Simulated Loading:** Animated spinner provides feedback while the script retrieves information.
- **Detailed IP Information:**
  - IP address
  - Hostname
  - City
  - Region
  - Country
  - Coordinates (latitude, longitude)
  - Organization
  - Postal code
  - Timezone
  - ASN (Autonomous System Number)
  - Continent name
- **Input Validation:** Ensures that the user inputs a valid IPv4 address before proceeding.

## Installation and Requirements

### Prerequisites

- **Bash Environment:** Ensure you are using a Unix-based shell (Linux, macOS, or Termux on Android).
- **`jq` JSON Processor:** A lightweight tool used to parse JSON API responses.
  - Installation:
    ```bash
    sudo apt install jq
    ```
- **API Key from ipgeolocation.io:** Required for ASN and continent information.
  - [Sign up](https://ipgeolocation.io/signup) for a free API key and replace `YOUR_API_KEY` in the script with your own.

## Usage

### Clone the Repository

First, download the script using Git:

```bash
git clone <repository-link>
cd <repository-folder>
```

### Run the Script

Execute the script using:

```bash
bash main.sh
```

### Input the IP Address

When prompted, enter a valid public IP address:

```bash
Please enter the IP address > 8.8.8.8
```

### Review the Output

The script will output detailed information regarding the IP address provided, including geolocation, ASN, and continent information.

#### Example Output:

```
Please enter the IP address > 8.8.8.8
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
------------------------------------------------------
```

## Error Handling

- **Invalid IP Format:** If an invalid IP format is entered, the script returns:
  ```
  [!] Invalid IP format! Please enter a valid IP.
  ```

- **Missing `jq`:** If `jq` is not installed, the script prompts the user:
  ```
  [!] jq is not installed. Install it with 'sudo apt install jq'.
  ```

## Rate Limits and Best Practices

Both ipinfo.io and ipgeolocation.io provide free-tier API services. Be aware of their rate limits, and consider upgrading to higher-tier plans if you intend to use the script for large-scale data collection.

## License

This project is open-source and available under the MIT License. You are free to use, modify, and distribute the script, but proper attribution to the author (LocalHost.07) is required.

## Version History

- **v1.0:** Initial release with full feature set.
- **v1.1:** Added ASN and continent support via ipgeolocation.io API.
- **v1.2:** Input validation and error handling improvements.
- **v1.3:** Optimized loading animation and error messaging.

---

## Contributions

Contributions are welcome! Feel free to submit issues, pull requests, or suggestions for new features and improvements.
"""

