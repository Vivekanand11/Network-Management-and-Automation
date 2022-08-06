from netmiko import ConnectHandler

def Router1():
    iosv2={
        'device_type':'cisco_ios',
        'ip':'198.51.100.3',
        'username':'lab',
        'password':'lab123'
    }
    net_connect = ConnectHandler(**iosv2)
    with open('/etc/ansible/Configs/R1.txt','r') as vivek:
      cassey=vivek.read()
      send_the_configs= cassey
      net_connect.send_config_set(send_the_configs)
      config_commands=['do sh ip int br']
      net_connect.enable()
      vivek1=net_connect.send_command(config_commands)
      return vivek1  

def Router2():
    iosv2={
        'device_type':'cisco_ios',
        'ip':'198.51.100.4',
        'username':'lab',
        'password':'lab123'
    }
    net_connect = ConnectHandler(**iosv2)
    with open('/etc/ansible/Configs/R2.txt','r') as vivek:
      cassey=vivek.read()
      send_the_configs= cassey
      net_connect.send_config_set(send_the_configs)
      config_commands=['do sh ip int br']
      net_connect.enable()
      vivek2=net_connect.send_command(config_commands)
      return vivek2    

def Router3():
    iosv2={
        'device_type':'cisco_ios',
        'ip':'198.51.100.5',
        'username':'lab',
        'password':'lab123'
    }
    net_connect = ConnectHandler(**iosv2)
    with open('/etc/ansible/Configs/R3.txt','r') as vivek:
      cassey=vivek.read()
      send_the_configs= cassey
      net_connect.send_config_set(send_the_configs)
      config_commands=['do sh ip int br']
      net_connect.emable()
      vivek3=net_connect.send_config_set(config_commands)
      return vivek3
if __name__=="__main__":
    x=Router1()
    print(x)
    y=Router2()
    print(y)
    z=Router3()
    print(z)