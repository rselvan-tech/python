orders=open('C:\\Users\\navaras2012\\Downloads\\Orders.txt').read().splitlines()
print(orders[:2])

order_items=open('C:\\Users\\navaras2012\\Downloads\\Order_Items.txt').read().splitlines()
print(order_items[:2])

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

def get_daily_revenue( all_orders, all_order_items):
    daily_revenue={}
    for o in all_orders:
        t_o=o.split(',')              # temp orders
        t_o_date=t_o[1][:10]          # temp order date
        print(f'{t_o_date=}')
        for oi in all_order_items:
            t_oi=oi.split(',')
            if t_oi[1]==t_o[0]:
                if t_o_date not in daily_revenue:
                    daily_revenue[t_o_date]=float(t_oi[4])
                else:
                    daily_revenue[t_o_date]+=float(t_oi[4])
    return(daily_revenue)

print(get_daily_revenue(orders,order_items))



