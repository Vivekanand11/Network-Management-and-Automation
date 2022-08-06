from easysnmp import Session
import json

def vivek():
    v1=['192.168.10.1', '192.168.10.2', '192.168.20.1','192.168.10.3', '192.168.10.4']
    v2=[]


    for x in range(len(v1)):
        session=Session(hostname=v1[x],community='public',version=1)
        ipaddress=session.walk('.1.3.6.1.2.1.4.20.1.2')
        for x in range(len(ipaddress)):
            v1.append(ipaddress[x].oid_index)
            return v2

def v6():
    v1=['192.168.10.1', '192.168.10.2', '192.168.20.1','192.168.10.3', '192.168.10.4']
    v2=[]
    v3=[]
    v4=[]
    v5=[]
    v6=[]
    v7=[]

    for x in range(len(v1)):
        session=Session(hostname=v1[x],community='public',version=1)
        ipaddress=session.walk('.1.3.6.1.2.1.4.34.1.2.3.16')
        for x in range(len(ipaddress)):
            output=ipaddress[x].oid_index
            v2.append(output)
    for x in range(len(v2)):
        any=v2[x].split(".")
        value=((any[2:]))
        v3.append(value)

    for k in range(8):
        for i in range(len(v3[k])):
            v4.append(((hex(int(v3[k][i])))))
        for i in range(len(v4)):
            v5.append(v4[i][2:])

        v6.append(v5[0:16])
        v6.extend((v5[16:32], v5[32:48], v5[48:64], v5[64:80], v5[80:96], v5[96:112], v5[112:128]))
        for i in range(len(v6)):
            test1=''.join(v6[i][0])
            test=''.join(v6[i][1])
            vivek=f'{test1}0{test}'
            g=''.join(v6[i][2:4])
            h=''.join(v6[i][4:6])
            i=''.join(v6[i][6:8])
            j=''.join(v6[i][8:10])
            k=''.join(v6[i][10:12])
            l=''.join(v6[i][12:14])
            m=''.join(v6[i][14:16])
            v7.append((f'{vivek}:{g}:{h}:{i}:{j}:{k}:{l}:{m}'))
            return(v7)
def interface_status():


    v1=['192.168.10.1', '192.168.10.2', '192.168.20.1','192.168.10.3', '192.168.10.4']
    v2=[]
    for i in range(len(v1)):
        session=Session(hostname=v1[i],community='public',version=1)
        ipaddress0=session.get('IF-MIB::ifName.1')
        ipaddress1=session.get('IF-MIB::ifName.2')
        ipaddress2=session.get('1.3.6.1.2.1.2.2.1.8.1')
        if ipaddress2.oid_index=='1':
            output="Interface is up"
        else:
            output="Interface is down"

        v2.append(f'{ipaddress0.value}:{output},{ipaddress1.value}:{output}')
        return v2
import json
from NMsnmp import vivek, v6, interface_status  
a=vivek()
b=v6()
c=interface_status()

def FILE():
    VIVEK={
        "R1":{
            "ADDRESSES":{
                "FA0/0":{
                    "V4":a[0],
                    "V6":b[0]
                }
            }
        },
        "R2":{
            "ADDRESSES":{
                "FA0/0":{
                    "V4":a[2],
                    "V6":b[2]
                },
                "FA1/0":{
                    "V4":a[1],
                    "V6":b[1]
                }
            }
        },
        "R3":{
            "ADDRESSES":{
                "FA0/0":{
                    "V4":a[4],
                    "V6":b[4]
                },
                "FA1/0":{
                    "V4":a[3],
                    "V6":b[3]
                }
            }
        },
        "R4":{
            "ADDRESSES":{
                "FA0/0":{
                    "V4":a[6],
                    "V6":b[6]
                },
                "FA1/0":{
                    "V4":a[5],
                    "V6":b[5]
                }
            }
        },
        "R5":{
            "ADDRESSES":{
                "FA0/0":{
                    "V4":a[8],
                    "V6":b[8]
                },
                "FA1/0":{
                    "V4":a[7],
                    "V6":b[7]
                }
            }
        },
        
    }
    VAIBHAV={"Router1":{"fa1/0":"up"}, "Router2":c[1], "Router3":c[2], "Router4":c[3],"Router5":{"fa0/0":"up"}

    

    
                }
    json_string = json.dumps(VIVEK,
                         skipkeys= True,
                         allow_nan = True,
                         indent = 6)
    json_string2 = json.dumps(VAIBHAV,
                         skipkeys= True,
                         allow_nan = True,
                         indent = 6)
    
    
    with open('jsonfile.txt','w') as file:
        file.write(json_string)
        file.write(json_string2)
    file.close()

if __name__=="__main__":
    a1=vivek()
    print(a1)
    b1=v6()
    print(b1)
    c1=interface_status()
    print(c1)