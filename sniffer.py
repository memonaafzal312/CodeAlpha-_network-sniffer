from scapy.all import sniff
from scapy.layers.inet import IP

def capture(packet):
    if packet.haslayer(IP):
        print("Source:", packet[IP].src)
        print("Destination:", packet[IP].dst)
        print("Protocol:", packet[IP].proto)
        print("-"*30)

sniff(count=10, prn=capture)