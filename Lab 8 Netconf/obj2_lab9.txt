from ncclient import manager
from prettytable import PrettyTable
import csv
def Router1():
    R1=manager.connect(
    host='198.51.100.11',
    port=22,
    username='lab',
    password='lab123',
    hostkey_verify=False,
    device_params={'name':'csr'})


    R1="""
     <config>
      <rpc message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1:0>
       <cli-config-data>
         <cmd>hostname Router1</cmd>
         <cmd>interface loopback99</cmd>
         <cmd>ip add 10.1.1.1 255.255.255.0</cmd>
         <cmd>router ospf 1</cmd>
         <cmd>network 10.1.1.0 0.0.0.255 area 0</cmd>
       </cli-config-data>
     <config>
     <</rpc>]]>]]>"""
    a=R1.edit_config(R1,target='running')
    #print(a)

def Router2():
    R2=manager.connect(
    host='198.51.100.12',
    port=22,
    username='lab',
    password='lab123',
    hostkey_verify=False,
    device_params={'name':'csr'})
    R2="""
     <config>
     <rpc message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1:0>
      <cli-config-data>
        <cmd>hostname Router2</cmd>
        <cmd>interface loopback99</cmd>
        <cmd>ip add 10.1.2.1 255.255.255.0</cmd>
        <cmd>router ospf 1</cmd>
        <cmd>network 10.1.2.0 0.0.0.255 area 0</cmd>
      </cli-config-data>
     <config>
     <</rpc>]]>]]>"""
    b=R2.edit_config(R2,target='running')
    #print(b)

def Router3():
    R3=manager.connect(
    host='198.51.100.13',
    port=22,
    username='lab',
    password='lab123',
    hostkey_verify=False,
    device_params={'name':'csr'})
    R3="""
     <config>
     <rpc message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1:0>
       <cli-config-data>
          <cmd>hostname Router3</cmd>
          <cmd>interface loopback99</cmd>
          <cmd>ip add 10.1.3.1 255.255.255.0</cmd>
          <cmd>router ospf 1</cmd>
          <cmd>network 10.1.3.0 0.0.0.255 area 0</cmd>
        </cli-config-data>
     <config>
     <</rpc>]]>]]>"""
    c=R3.edit_config(R3,target='running')
    #print(c)

def Router4():
    R4=manager.connect(
    host='198.51.100.14',
    port=22,
    username='lab',
    password='lab123',
    hostkey_verify=False,
    device_params={'name':'csr'})


    R4="""
     <config>
     <rpc message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1:0>
       <cli-config-data>
         <cmd>hostname Router4</cmd>
         <cmd>interface loopback99</cmd>
         <cmd>ip add 10.1.4.1 255.255.255.0</cmd>
         <cmd>router ospf 1</cmd>
         <cmd>network 10.1.4.0 0.0.0.255 area 0</cmd>
       </cli-config-data>
     <config>
     </rpc>]]>]]>"""
    d=R4.edit_config(R4,target='running')
    #print(d)

def Router5():
    R5=manager.connect(
    host='198.51.100.15',
    port=22,
    username='lab',
    password='lab123',
    hostkey_verify=False,
    device_params={'name':'csr'})
    R5="""
     <config>
     <rpc message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1:0>
       <cli-config-data>
             <cmd>hostname Router5</cmd>
             <cmd>interface loopback99</cmd>
             <cmd>ip add 10.1.5.1 255.255.255.0</cmd>
             <cmd>router ospf 1</cmd>
             <cmd>network 10.1.5.0 0.0.0.255 area 0</cmd>
       </cli-config-data>
     <config>
     </rpc>]]>]]>"""
    e=R5.edit_config(R5,target='running')
    #print(e)

def netconfig_config(lab9-obj2-conf.csv):
    vaibhav=open(lab9-obj2-conf.csv)
    vaibhav=PrettyTable()
    vaibhav.field_names=['Hostname','loopback99 IP','ip add','subnet mask','OSPF network to advertise','area']
    vaibhav.add_row(['Router1','loopback99','10.1.1.1','255.255.255.0','10.1.1.0 0.0.0.255','0'])
    vaibhav.add_row(['Router2','loopback99','10.1.2.1','255.255.255.0','10.1.2.0 0.0.0.255','0'])
    vaibhav.add_row(['Router3','loopback99','10.1.3.1','255.255.255.0','10.1.3.0 0.0.0.255','0'])
    vaibhav.add_row(['Router4','loopback99','10.1.4.1','255.255.255.0','10.1.4.0 0.0.0.255','0'])
    vaibhav.add_row(['Router5','loopback99','10.1.5.1','255.255.255.0','10.1.5.0 0.0.0.255','0'])
    print(vaibhav)
if __name__=="__main__":
    netconfig_config()