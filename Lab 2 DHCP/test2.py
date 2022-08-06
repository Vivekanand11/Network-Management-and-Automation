from scapy.all import *
src = '198.51.100.2'
dst = '198.51.100.1'
sport = random.randint(1024, 65535)
dport= 23
ip = IP(src=src, dst=dst)
SYN=TCP(sport=sport,dport=dport,flags='S',seq=1000)
SYNACK=sr1(ip/SYN)
ip.show()
SYN.show()
SYNACK.show()