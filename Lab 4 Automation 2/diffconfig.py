from napalm import get_network_driver

driver = get_network_driver("ios")
iosv=driver("198.51.100.5", 'vivek', 'vivek456')
iosv.open()
ios_output = iosv.get_config()['running']
difference = iosv.compare_config()
if len(difference)>0:
    print(f'The difference is:{difference}')
    iosv.commit_config()
else:
        print("there is no any difference in the config")

iosv.close()

driver = get_network_driver("ios")
iosv=driver("198.51.100.6", 'vivek', 'vivek456')
iosv.open()
ios_output = iosv.get_config()['running']
difference = iosv.compare_config()
if len(difference)>0:
    print(f'The difference is:{difference}')
    iosv.commit_config()
else:
        print("there is no  any difference in the config")

iosv.close()

driver = get_network_driver("ios")
iosv=driver("198.51.100.7", 'vivek', 'vivek456')
iosv.open()
ios_output = iosv.get_config()['running']
difference = iosv.compare_config()
if len(difference)>0:
    print(f'The difference is:{difference}')
    iosv.commit_config()
else:
        print("there is no any difference in the config")

iosv.close()

driver = get_network_driver("ios")
iosv=driver("198.51.100.8", 'vivek', 'vivek456')
iosv.open()
ios_output = iosv.get_config()['running']
difference = iosv.compare_config()
if len(difference)>0:
    print(f'The difference is:{difference}')
    iosv.commit_config()
else:
        print("there is no any difference in the config")

iosv.close()