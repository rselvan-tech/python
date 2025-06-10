from myFilter import myFilter
from myMap import myMap
from myReduce import myReduce

#get the sum of sub totals for a given order id

order_items=open('C:\\Users\\navaras2012\\Downloads\\Order_Items.txt').read().splitlines()
#print(order_items[:2])

'''
Order Items File
================
- order_item_id
- order_item_order_id
- order_item_product_id
- order_item_quantity
- order_item_subtotal
- order_item_product_price
'''

filter_res=myFilter(order_items, lambda oi: oi.split(',')[1]=='2')
map_res=myMap(filter_res, lambda n: float(n.split(',')[4]))
sub_total=myReduce(map_res, lambda x,y: x+y)
print(f'{filter_res=}')
print(f'{map_res=}')
print(f'{sub_total=}')
