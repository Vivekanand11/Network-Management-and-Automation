from napalm import get_network_driver
from prettytable import PrettyTable
def vivek():
    driver = get_network_driver("ios")
    device=driver("198.51.100.5", "vivek","vivek456", optional_args={'global_delay_factor':4})
    device.open()
    device.load_merge_candidate(config='router ospf 1\n network 198.51.101.0 0.0.0.255 area 1\n network 198.51.100.0 0.0.0.255 area 1\n network 10.0.0.0 0.0.0.0 area 1\n no shutdown\n end\n')
    a=device.commit_config()
    print(a)
    device.close()

    driver = get_network_driver("ios")
    device=driver("198.51.100.6", "vivek","vivek456", optional_args={'global_delay_factor':4})
    device.open()
    device.load_merge_candidate(config='router ospf 1\n network 198.51.101.0 0.0.0.255 area 1\n 172.16.1.0 0.0.0.255 area 0\n network 20.0.0.0 0.0.0.0 area 1\n no shutdown\n end\n')
    b=device.commit_config()
    print(b)
    device.close()

    driver = get_network_driver("ios")
    device=driver("198.51.100.7", "vivek","vivek456", optional_args={'global_delay_factor':4})
    device.open()
    device.load_merge_candidate(config='router ospf 1\n network 172.16.1.0 0.0.0.255 area 0\n network 198.51.101.0 0.0.0.255 area 1 \n network 40.0.0.0 0.0.0.0 area 1\n no shutdown\n end\n')
    c=device.commit_config()
    print(c)
    device.close()

    driver = get_network_driver("ios")
    device=driver("198.51.100.8", "vivek","vivek456", optional_args={'global_delay_factor':4})
    device.open()
    device.load_merge_candidate(config='router ospf 1\n network 172.16.1.0 0.0.0.255 area 0\network 30.0.0.0 0.0.0.0 area 0\n no shutdown\n end\n')
    d=device.commit_config()
    print(d)
    device.close()
def prettytable1():
 v=PrettyTable()
 v.field_names = ["Routername", "IPaddress", "Interfaces"]
 v.add_row(["R1", "198.51.100.5", "fa0/0"])
 v.add_row(["R1", "198.51.101.3", "fa1/0"])
 v.add_row(["R2", "198.51.101.3", "fa0/0"])
 v.add_row(["R2", "172.16.1.1", "fa1/0"])
 v.add_row(["R3", "172.16.1.4", "fa0/0"])
 v.add_row(["R4", "172.16.1.2", "fa1/0"])
 v.add_row(["R4", "198.51.101.4", "fa1/1"])
 print(v)

def main():
    prettytable1()

if __name__ == "__main__":
    main()
