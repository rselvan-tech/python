orders=open('C:\\Users\\navaras2012\\Downloads\\Orders.txt').read().splitlines()

'''
Orders File
================
- order_id
- order_date
- customer_id
- order_status
'''
def get_count_by_order_status(all_orders):
    order_status={}

    for order in all_orders:
        temp_order=order.split(',')

        if temp_order[3] not in order_status:
            order_status[temp_order[3]]=1
        else:
            order_status[temp_order[3]] +=1
    return order_status

print(get_count_by_order_status(orders))


