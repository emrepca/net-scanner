import scapy.all as scapy
import optparse
import requests

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--ipaddress", dest="ip_address", help="Enter Ip Address")

    (user_input, arguments) = parse_object.parse_args()
    if not user_input.ip_address:
        print("Enter Ip Address")

    return user_input


def scan_my_network(ip):
    arp_request_packet = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packet = broadcast_packet / arp_request_packet
    answered_list = scapy.srp(combined_packet, timeout=1)[0]

    return answered_list


def get_mac_vendors(mac_address):
    mac_address = mac_address[0][1].hwsrc[:8]
    url = f"https://api.macvendors.com/{mac_address}"
    try:
        response = requests.get(url)
        if response.status_code == 200: #successful response
            return response.text.strip()

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

    return "Unknown"


user_ip_address = get_user_input()
answered_list = scan_my_network(user_ip_address.ip_address)

for i in range(28):
    print("- ", end="")
for result in answered_list:
    vendors = get_mac_vendors(result)
    print("\n")
    print(f"Ip Address: {result[0].psrc} \t Mac Address: {result[0][1].hwsrc} \t MAC Address Vendors: {vendors}")
print("\n")
for i in range(28):
    print("- ", end="")
