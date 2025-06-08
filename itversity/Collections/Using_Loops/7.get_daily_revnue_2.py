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

def get_daily_revenue(all_orders, all_order_items):
    daily_revenue = {}

    # Build a map from order_item_order_id to all order items for faster lookup
    order_items_map = {}
    for oi in all_order_items:
        t_oi = oi.split(',')
        order_id = t_oi[1]
        subtotal = float(t_oi[4])
        order_items_map.setdefault(order_id, []).append(subtotal)

    for o in all_orders:
        t_o = o.split(',')
        order_id = t_o[0]
        order_date = t_o[1][:10]  # Use first 10 chars for YYYY-MM-DD

        # Sum all subtotals for this order_id
        order_total = sum(order_items_map.get(order_id, []))

        if order_date not in daily_revenue:
            daily_revenue[order_date] = order_total
        else:
            daily_revenue[order_date] += order_total
    return daily_revenue

print(get_daily_revenue(orders,order_items))

'''
setdefault()
************
What this does:
order_items_map is a dictionary where:

keys are order_id strings. values are lists of subtotal amounts (floats).

Step-by-step explanation:
order_items_map.setdefault(order_id, [])

The setdefault method looks for the key order_id in the dictionary.

If order_id already exists as a key, it returns the current value (which should be a list).

If order_id does not exist, it:

Creates a new entry in the dictionary with key order_id and value set to the empty list [].

Then returns this new empty list.

.append(subtotal)

After setdefault returns the list (either existing or newly created empty list), .append(subtotal) adds the current subtotal value to that list.

Why use setdefault here?
To avoid checking if the key exists explicitly.

Without setdefault, you would do something like:
    if order_id not in order_items_map:
        order_items_map[order_id] = []
    order_items_map[order_id].append(subtotal)
Using setdefault is a concise way to do this in one line.
'''

'''
get()
*****
get(self, key, default=None, /) unbound builtins.dict method
    Return the value for key if key is in the dictionary, else default.

sum(None) => TypeError: 'NoneType' object is not iterable

by dedault get() retuns None if no key found. and None will result in TypeError for sum

hence need to reurn empty [] when no key found
order_total = sum(order_items_map.get(order_id, []))

'''