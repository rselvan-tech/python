'''
Challenge #1

Consider the following string declaration which is part of the output of a Linux command.

my_str = 'wlo1 Link encap:Ethernet HWaddr b4:6d:83:77:85:f3'

Write a Python script that extracts the MAC address (b4:6d:83:77:85:f3) from the string.

Try to solve the challenge in more than one way.
'''
my_str = 'wlo1 Link encap:Ethernet HWaddr b4:6d:83:77:85:f3'

str_pos=my_str.find('HWaddr')
#help(str.find)
if str_pos != -1:
    mac_pos=str_pos+len('HWaddr ')
    print(f'MAC Address : { my_str[mac_pos:]}')