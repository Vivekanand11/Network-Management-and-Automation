from scapy.all import *
ethernet=Ether(dst='ff:ff:ff:ff:ff:ff', type=0x800)
ip = IP(src='0.0.0.0', dst='255.255.2255.255')
ports = UDP(sport=68, dport=67)
fam, hw = get_if_raw_hwaddr('tap0')
bootp=BOOTP(chaddr=hw, ciaddr='0.0.0.0', xid=0x01020304, flags=1)
dhcp=DHCP(options=[('message-type','discover'), 'end'])
srp(ethernet/ip/ports/bootp/dhcp, iface='tap0')
srp.show()
