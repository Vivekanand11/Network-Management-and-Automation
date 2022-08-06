from napalm import get_network_driver
from netmiko import ConnectHandler
from NMtcpdump import tom1, tom2
import re
def jerry():
    vivek1=tom1()
    vivek2=tom2()
    driver=get_network_driver('ios')
    iosv1=driver('3001:1234:A:B:1::','vivek', 'vivek123')
    iosv1.open()
    vivek3=iosv1.get_ipv6_neighbors_table()
    for x in vivek3:
        if x['interface']=="Fa0/0" and "fe80::" not in x['ip'] and x['ip']!=vivek1 and x['ip']!=vivek2:
            return(x['ip'])

def R5():
   vivek=jerry()
   iosv2={
        'device_type':'cisco_ios',
        'ip':vivek,
        'username':'vivek',
        'password':'vivek123'
   }
   net_connect=ConnectHandler(**iosv2)
   configuration=['int fa0/0', 'ip address 192.168.10.1 255.255.255.0', 'no shut', 'exit', 'ip dhcp pool vivek','network 192.168.10.0']
   output=net_connect.send_config_set(configuration)
   ipv4address=net_connect.send_command('show ip dhcp binding')
   vivek3=re.findall('\d\d\d.\d\d\d.\d\d.\d', ipv4address)
   return vivek3

if __name__=="__main__":
   a=R5()
   print(f"list of IPv4 addresses from clients is:{a}")










