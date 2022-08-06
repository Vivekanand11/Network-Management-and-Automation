from scapy.all import *
from scapy.layers.inet6 import ICMPv6EchoRequest, ICMPv6ND_NA, ICMPv6ND_RA, ICMPv6ND_RS

i=IPv6()
i.dst="2001:0BB9:AABB:1234::"
q=ICMPv6EchoRequest()
p=(i/q)
sr1(p)
ls(ICMPv6ND_RA)
ls(ICMPv6ND_RS)
ls(ICMPv6ND_NA)