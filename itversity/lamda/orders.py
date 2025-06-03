orders=open('C:\\Users\\navaras2012\\Downloads\\Orders.txt').read().splitlines()
print(type(orders))
print(len(orders))
print(orders[:10])

def get_order_date(o):
    return o.split(',')[1]

print(get_order_date(orders[0]))

#print(get_order_date(orders))
print(list(map(get_order_date,orders))[:10])
print(list(map(lambda s: s.split(',')[1],orders))[:10])

