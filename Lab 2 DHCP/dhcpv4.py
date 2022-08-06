from netmiko import ConnectHandler
import threading
import time

def Router2():
    iosv2={
        'device_type':'cisco_ios',
        'ip':'198.51.100.50',
        'username':'vivekdhondji',
        'password':'vidh2092'
    }
    net_connect = ConnectHandler(**iosv2)
    configuration_commands1 = ['int f0/0', 'ip address dhcp', 'no shut', 'exit']
    net_connect.send_config_set(configuration_commands1)
    time.sleep(10)
    config_commands= ['do show ip interface brief']
    net_connect.enable()
    a=net_connect.send_config_set(config_commands)
    print(a)

def Router3():
    iosv2={
        'device_type':'cisco_ios',
        'ip':'198.51.100.60',
        'username':'vivekdhondji',
        'password':'vidh2092'
    }
    net_connect = ConnectHandler(**iosv2)
    configuration_commands1 = ['int f0/0', 'ip address dhcp', 'no shut', 'exit']
    net_connect.send_config_set(configuration_commands1)
    time.sleep(10)
    config_commands= ['do show ip interface brief']
    net_connect.enable()
    b=net_connect.send_config_set(config_commands)
    print(b)   

def Router4():
    iosv2={
        'device_type':'cisco_ios',
        'ip':'198.51.100.70',
        'username':'vivekdhondji',
        'password':'vidh2092'
    }
    net_connect = ConnectHandler(**iosv2)
    Configuration_commands1 = ['int f0/0', 'ip address dhcp', 'no shut', 'exit']
    net_connect.send_config_set(Configuration_commands1)
    time.sleep(10)
    config_commands= ['do show ip interface brief']
    net_connect.enable()
    c=net_connect.send_config_set(config_commands)
    print(c)

p1=threading.Thread(target=Router2)
p2=threading.Thread(target=Router3)
p3=threading.Thread(target=Router4)
p1.start()
p2.start()
p3.start()
