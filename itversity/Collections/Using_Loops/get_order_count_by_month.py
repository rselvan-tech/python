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


def get_order_count_by_month(all_orders, order_status):
    order_count_per_month={}
    for order in all_orders:
        temp_order=order.split(',')

        if temp_order[3]==order_status:
            temp_order_month=temp_order[1][:7]
            if temp_order_month not in order_count_per_month:
                order_count_per_month[temp_order_month]=1
            else:
                order_count_per_month[temp_order_month]+=1
    
    return(order_count_per_month)

print(get_order_count_by_month(orders,'PENDING'))

'''
order_count_per_month={}
order_count_per_month['2013-05']=1
print(order_count_per_month)
print(type(order_count_per_month['2013-05']))
'''