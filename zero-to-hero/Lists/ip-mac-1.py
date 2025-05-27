interface = '''wlo1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.0.105  netmask 255.255.255.0  broadcast 192.168.0.255
        inet6 fe80::6ec6:fea5:4a08:33ae  prefixlen 64  scopeid 0x20<link>
        ether 14:13:33:ee:9c:1b  txqueuelen 1000  (Ethernet)
        RX packets 1007942  bytes 902567350 (902.5 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 531217  bytes 158518152 (158.5 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0'''

#help(str.find)
ipv4_start= interface.find('inet')+len('inet ')
ipv4_end=interface.find(' ',ipv4_start)
ipv4=interface[ipv4_start:ipv4_end+1]
print(f'ipv4 = {ipv4}')

ipv6_start= interface.find('inet6')+len('inet6 ')
ipv6_end=interface.find(' ',ipv6_start)
ipv6=interface[ipv6_start:ipv6_end+1]
print(f'ipv6 = {ipv6}')

mac_start= interface.find('ether')+len('ether ')
mac_end=interface.find(' ',mac_start)
mac=interface[mac_start:mac_end+1]
print(f'mac = {mac}')