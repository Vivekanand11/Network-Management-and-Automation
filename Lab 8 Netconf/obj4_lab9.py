from ncclient import manager
v=manager.connect(
    host='198.51.100.1',
    port=22,
    username='netman',
    password='netman',
    hostkey_verify=False,
    device_params={'name':'iosxr'})

def obj4():
  VIVEK= """
   <config>
   <rpc message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1:0>

   <config>
     <cli-config-data>

       <cmd> hostname Lab9_XR</cmd>
       <cmd> interface Loopback1</cmd>
       <cmd> ip add 10.11.12.13 255.255.255.255</cmd>
       <cmd> access-list 1 permit 198.51.100.2</cmd>
     </cli-config-data>
   </config>
 </rpc>]]>]]>"""

  k=v.edit_config(VIVEK,target='running')
  print(k)


if __name__== "__main__":
  obj4()