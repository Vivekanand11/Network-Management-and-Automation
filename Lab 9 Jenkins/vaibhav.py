import unittest

try:
    from ncclient import manager
    from netaddr import IPAddress
except Exception:
    print('Install all the necessary modules')
FETCH_INFO = '''
    		<filter>
    		<config-format-text-block>
    		<text-filter-spec> %s </text-filter-spec>
    		</config-format-text-block>
    		</filter>
    		'''

class unittesting(unittest.TestCase):

    def test_ip(self):
        connection = manager.connect(host='198.51.100.13',
                                    port=22,
                                    username='lab',
                                    password='lab123',
                                    hostkey_verify=False,
                                    device_params={'name': 'iosxr'},
                                    allow_agent=False,
                                    look_for_keys=True)

        

        fetch_lo_info = FETCH_INFO % ('int Loopback99')
        output2 = connection.get_config('running', fetch_lo_info)
        split2 = str(output2).split()
        lo_ip_mask = split2[9] + '/' + str(IPAddress(split2[10]).netmask_bits())
        self.assertEqual('10.1.3.1/24', lo_ip_mask)
    def test_config(self):
        connection = manager.connect(host='198.51.100.11',
                                    port=22,
                                    username='lab',
                                    password='lab123',
                                    hostkey_verify=False,
                                    device_params={'name': 'iosxr'},
                                    allow_agent=False,
                                    look_for_keys=True)
        fetch_ospf_info = FETCH_INFO % ('| s ospf')
        output3 = connection.get_config('running', fetch_ospf_info)
        split3 = str(output3).split()
        area=[]
        for l in range(len(split3)):
            if split3[l]=='area':
                area.append(split3[l+1])
        self.assertTrue(all(v==area[0] for v in area))

    def test_ping(self):
        connection = manager.connect(host='198.51.100.12',
                                    port=22,
                                    username='lab',
                                    password='lab123',
                                    hostkey_verify=False,
                                    device_params={'name': 'iosxr'},
                                    allow_agent=False,
                                    look_for_keys=True)
        #fetch_lo_info = FETCH_INFO % ('int Loopback99')
        #output2 = connection.get_config('running', fetch_lo_info)
        self.assertTrue('ping 10.1.5.1')

if __name__=="__main__":
    unittest.main()
