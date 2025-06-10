from myFilter import myFilter
from myMap import myMap
from myReduce import myReduce
from myReduceByKey import myReduceByKey

#Read "Orders.txt" File into a list object
orders=open('C:\\Users\\navaras2012\\Downloads\\Orders.txt').read().splitlines()
#print(orders[:2])

#Read "Order_items.txt" File into a list object
order_items=open('C:\\Users\\navaras2012\\Downloads\\Order_Items.txt').read().splitlines()
#print(order_items[:2])

'''
Orders File
================
- order_id
- order_date
- customer_id
- order_status

Order Items File
================
- order_item_id
- order_item_order_id
- order_item_product_id
- order_item_quantity
- order_item_subtotal
- order_item_product_price
'''

#Get number of COMPLETE orders placed by each customer
#Get total number of PENDING and PENDING_PAYMENT orders for the month of 2014 January
#Get outstanding amount for each month considering orders with status PAYMENT_REVIEW,PENDING,PENDING_PAYMENT and PROCESSING