"""

Resultado:

IP & MAC Address
----------------------------------------
10.0.2.2    52:54:00:12:35:02
10.0.2.3    52:54:00:12:35:03
10.0.2.4    52:54:00:12:35:04
----------------------------------------

"""

import scapy.all as scapy

arp_request = scapy.ARP(pdst="10.0.2.15/24")
broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
arp_request_packet = broadcast/arp_request

answered_list = scapy.srp(arp_request_packet, timeout=2, verbose=False)[0]

print("IP & MAC Address")
print("-" * 40)
for element in answered_list:
    print(element[1].psrc + "\t" + element[1].hwsrc)
print("-" * 40)