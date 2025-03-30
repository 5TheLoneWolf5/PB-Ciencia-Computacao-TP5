import scapy.all as scapy

ip_mac_mapping = {}

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    ether_frame = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = ether_frame / arp_request
    response = scapy.srp(arp_request_broadcast, timeout=2, verbose=False)[0]
    
    if response:
        return response[0][1].hwsrc
    return None

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def process_sniffed_packet(packet):
    if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op == 2:

        ip_src = packet[scapy.ARP].psrc
        mac_src = packet[scapy.ARP].hwsrc

        if ip_src not in ip_mac_mapping:
            real_mac = get_mac(ip_src)
            if real_mac:
                ip_mac_mapping[ip_src] = real_mac

        if ip_src in ip_mac_mapping and ip_mac_mapping[ip_src] != mac_src:
            print(f"Alerta: Possível ARP Spoofing detectado para IP {ip_src} MAC anterior: {ip_mac_mapping[ip_src]}, MAC atual: {mac_src}")

if __name__ == "__main__":
    sniff("enp0s3")
