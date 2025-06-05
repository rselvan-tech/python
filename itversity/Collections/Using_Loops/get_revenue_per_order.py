order_items=open('C:\\Users\\navaras2012\\Downloads\\Order_Items.txt').read().splitlines()
print(order_items[:2])

'''
Order Items File
================
- order_item_id
- order_item_order_id
- order_item_product_id
- order_item_quantity
- order_item_subtotal
- order_item_product_price

Orders File
================
- order_id
- order_date
- customer_id
- order_status
'''

def get_revenue_per_order(all_order_items):
    revenue_per_order={}

    for item in all_order_items:
        temp_item=item.split(',')

        if temp_item[1] not in revenue_per_order:
            revenue_per_order[temp_item[1]]=float(temp_item[4])
        else:
            revenue_per_order[temp_item[1]]+=float(temp_item[4])
    return revenue_per_order

print(get_revenue_per_order(order_items))