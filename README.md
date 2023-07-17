# Network Scanner

  

This is a simple network scanner script written in Python. It uses Scapy library to perform an ARP scan on a given IP address or range of IP addresses and displays the IP addresses, MAC addresses, and MAC address vendors of the devices found on the network.

  

## Installation

  

1. Clone the repository:
  


	+ git clone https://github.com/your-username/network-scanner.git


2. Change to the project directory:

  

	+ cd network-scanner

  

3. Install the required dependencies:

  

	+ pip install -r requirements.txt

  

## Usage

  

Run the script with the following command:

  

+ python net_scanner.py -i <ip_address>

  

Replace `<ip_address>` with the IP address or IP address range you want to scan.

  

## Example

  

To scan the network for devices with IP address range `192.168.1.1/10`, run the following command:

  

+ ```python network_scanner.py -i 192.168.1.1/10```
+ ```python network_scanner.py -ipaddress 192.168.1.1/10```
