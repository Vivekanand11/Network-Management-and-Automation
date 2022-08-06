from pysnmp.hlapi import *
#from tkinter import *
R1 = getCmd(SnmpEngine(),
    CommunityData('public'),
    UdpTransportTarget(('198.51.100.5', 161)), 
    ContextData(), 
    ObjectType(ObjectIdentity('1.3.6.1.2.1.1.4.0')),
    ObjectType(ObjectIdentity('1.3.6.1.2.1.1.5.0')),
    ObjectType(ObjectIdentity('1.3.6.1.2.1.1.6.0')),
    ObjectType(ObjectIdentity('1.3.6.1.2.1.2.1.0')),
    ObjectType(ObjectIdentity('1.3.6.1.2.1.1.3.0')))
errorIndication, errorStatus, errorIndex, varBinds = next(R1)

if errorIndication:
    print(errorIndication)
elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) -1[0] or '?']))
else:
    for i,v in varBinds:
        print(v)
R2= getCmd(SnmpEngine(),
    CommunityData('public'),
    UdpTransportTarget(('198.51.100.6', 161)), 
    ContextData(), 
    ObjectType(ObjectIdentity('1.3.6.1.2.1.1.4.0')),
    ObjectType(ObjectIdentity('1.3.6.1.2.1.1.5.0')),
    ObjectType(ObjectIdentity('1.3.6.1.2.1.1.6.0')),
    ObjectType(ObjectIdentity('1.3.6.1.2.1.2.1.0')),
    ObjectType(ObjectIdentity('1.3.6.1.2.1.1.3.0')))
errorIndication, errorStatus, errorIndex, varBinds = next(R2)
if errorIndication:
    print(errorIndication)
elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) -1[0] or '?']))
else:
    for i,v in varBinds:
        print(v)

R3 = getCmd(SnmpEngine(),
    CommunityData('public'),
    UdpTransportTarget(('198.51.100.7', 161)), 
    ContextData(), 
    ObjectType(ObjectIdentity('1.3.6.1.2.1.1.4.0')),
    ObjectType(ObjectIdentity('1.3.6.1.2.1.1.5.0')),
    ObjectType(ObjectIdentity('1.3.6.1.2.1.1.6.0')),
    ObjectType(ObjectIdentity('1.3.6.1.2.1.2.1.0')),
    ObjectType(ObjectIdentity('1.3.6.1.2.1.1.3.0')))
errorIndication, errorStatus, errorIndex, varBinds = next(R3)
if errorIndication:
    print(errorIndication)
elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) -1[0] or '?']))
else:
    for i,v in varBinds:
        print(v)
