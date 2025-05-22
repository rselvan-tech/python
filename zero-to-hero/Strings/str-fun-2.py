# https://docs.python.org/3/library/stdtypes.html#string-methods

my_str='I learn Python Programming'

#1) str.upper()

print(my_str.upper())                #I LEARN PYTHON PROGRAMMING

#2) str.lower()

print(my_str.lower())                #i learn python programming

#3) str.strip()

ip='    123.45.56.78   '
print(ip.strip())                     #123.45.56.78

value='$$$45$$$$'
print(value.strip('$'))               #45

#4) str.replace()

new_value=value.replace('$','#')
print(value)                          #$$$45$$$$
print(new_value)                      ####45####

#5) str.count()
txt1='I learn Python and Python is cool'
n=txt1.count('Python')
print(n)                              #2

txt2='I learn PYthon and PyTHon is cool'
n=txt2.lower().count('python')
print(n)                              #2

n=txt2.count('o')
print(n)                              #4


#6) str.split()

my_list=txt1.split()
print(my_list)                        #['I', 'learn', 'Python', 'and', 'Python', 'is', 'cool']

txt3='I lea rn      PYthon and PyTH\non is cool'
print(txt3.split())                   #['I', 'lea', 'rn', 'PYthon', 'and', 'PyTH', 'on', 'is', 'cool']

print('192.45.3.56'.split('.'))       #['192', '45', '3', '56']

#7) str.join()

ip='192.45.3.56'
ip_list=ip.split('.')                 #['192', '45', '3', '56']

print(ip_list)

ip_str1='-'.join(ip_list)             #192-45-3-56
print(ip_str1)

ip_str2='<<XXX>>'.join(ip_list)       #192<<XXX>>45<<XXX>>3<<XXX>>56
print(ip_str2)

#8) str.find()
txt='I learn Python and Python is cool'

print(txt.find('Python'))             #8   index position of substr
print(txt.find('PYthon'))             #-1   substr not found

#9) in & not in

print('Python' in txt)                #True   substr found 
print('golang' in txt)                #Fale   substr not found 

#10) str.removeprefix() & str.removesuffix()

url='https://www.google.com'

cleaned_url=url.removeprefix('https://')
print(cleaned_url)                    #www.google.com

fname='final_report.pdf'
cleaned_fname=fname.removesuffix('.pdf')
print(cleaned_fname)                  #final_report





