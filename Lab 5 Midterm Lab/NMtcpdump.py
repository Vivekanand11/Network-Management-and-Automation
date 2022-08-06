from scapy.all import *
def tom1():
    a=rdpcap('vivek.pcap')
    cassey1=a[1]['IPv6'].src
    return cassey1

def tom2():
    b=rdpcap('vivek.pcap')
    cassey1=b[16]["IPv6"].src
    return cassey1

def tom(cassey1):
    ipv6p=cassey1.split(":")
    mac = []
    for i in ipv6p[-4:]:
        while len(i) < 4:
          i= "0" + i
        mac.append(i[:2])
        mac.append(i[-2:])
    mac[0] = "%02x" % (int(mac[0], 16) ^2)
    del mac[4]
    del mac[3]

    return ":".join(mac)

if __name__=="__main__":
    vivek=tom1()
    vivek1=tom(vivek)
    vivek2=tom2()
    vivek3=tom(vivek2)
    print(f"mac addres of R2 is : {vivek1}\nmac address of R3 is: {vivek3}")