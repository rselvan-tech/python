names_list = ['Alice', 'Bob', 'Eve']
 
## Converting list to string
names_str = ','.join(names_list)
print(f'{names_list=}\n{names_str=}')
 
url= 'www.python.org'
 
## Converting string to list
url_list = url.split('.')
print(f'{url=}\n{url_list=}')