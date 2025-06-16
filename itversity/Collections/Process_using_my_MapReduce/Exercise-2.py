from myFilter import myFilter
from myMap import myMap
from myReduce import myReduce
from myReduceByKey import myReduceByKey

#Read "Orders.txt" File into a list object
orders=open('C:\\Users\\navaras2012\\Downloads\\Orders.txt').read().splitlines()
#print(orders[:5])

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

#(1)Get number of COMPLETE orders placed by each customer
filter_orders=myFilter( orders,
                        lambda o: o.split(',')[3]=='COMPLETE' 
                      )
map_orders=myMap( filter_orders,
                  lambda o: ( int(o.split(',')[2]), 1)
                )
complete_orders_count=myReduceByKey( map_orders,
                                     lambda x,y: x+y 
                                   )
print(f'{complete_orders_count}=')
#(2)Get total number of PENDING and PENDING_PAYMENT orders for the month of 2014 January

filter_orders1=myFilter( orders,
                        lambda o: ( o.split(',')[3]=='PENDING') or ( o.split(',')[3]=='PENDING_PAYMENT') 
                      )
map_orders1=myMap( filter_orders1,
                  lambda o: ( o.split(',')[1][:10], 1)
                )
orders_count_2=myReduceByKey( map_orders1,
                                     lambda x,y: x+y 
                                   )
print(f'{orders_count_2}=')


#(3)Get outstanding amount for each month considering orders with status PAYMENT_REVIEW,PENDING,PENDING_PAYMENT and PROCESSING
filter_orders2=myFilter( orders,
                         lambda o: ( o.split(',')[3]=='PAYMENT_REVIEW') 
                                     or ( o.split(',')[3]=='PENDING')
                                     or ( o.split(',')[3]=='PENDING_PAYMENT')
                                     or ( o.split(',')[3]=='PROCESSING')
                      )
map_orders2=myMap( filter_orders2,
                  lambda o: (  o.split(',')[0], o.split(',')[1][:10] )
                )

order_month_dict=dict(map_orders2)
print(list(order_month_dict.items())[:2])

filter_order_items=myFilter(order_items ,
                         lambda oi: oi.split(',')[1] in order_month_dict) 

print(filter_order_items[:2])
map_order_items=myMap( filter_order_items,
                       lambda oi: ( order_month_dict[oi.split(',')[1]],float(oi.split(',')[4]) )
                      )
print(map_order_items[:2])
outstanding_amount=myReduceByKey( map_order_items,
                                  lambda x,y: round(x+y,2)
                                 )
print(outstanding_amount[:5])