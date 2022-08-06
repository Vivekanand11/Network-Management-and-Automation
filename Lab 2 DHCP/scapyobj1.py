from scapy.all import *
s=IP(dst="198.51.100.1")/ICMP()
send(s,loop=1, verbose=0)