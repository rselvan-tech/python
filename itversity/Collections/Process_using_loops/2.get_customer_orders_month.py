orders=open('C:\\Users\\navaras2012\\Downloads\\Orders.txt').read().splitlines()
print(orders[:2])

'''
Orders File
================
- order_id
- order_date
- customer_id
- order_status
'''
# order_month='YYYY-MM'

def get_customer_orders_month(all_orders,cust_id,order_month):
    cust_orders=[]

    for order in all_orders:
        temp_order=order.split(',')
        if temp_order[2] == cust_id and temp_order[1].startswith(order_month):
            cust_orders.append(order)
    return cust_orders

print(get_customer_orders_month(orders,'11599','2013-10'))
