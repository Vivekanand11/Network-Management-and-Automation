import csv
import yaml

with open('/home/netman//Documents/1.csv',newline='')as carrier:
  vivek=open('/etc/ansible/roles/router/vars/main.yaml','a')
  vivek.write('---\nrouters:\n')
  vaihav=csv.reader(carrier)
  archer=next(vaihav)
  for i in vaihav:
    yaml.dump([dict(zip(archer, i))], vivek, default_flow_style=False)
