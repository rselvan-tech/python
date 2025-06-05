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
def get_customer_orders(all_orders,cust_id):
    cust_orders=[]
    for order in all_orders:
        if order.split(',')[2] == cust_id:
            cust_orders.append(order)
    return cust_orders

print(get_customer_orders(orders,'11599'))


