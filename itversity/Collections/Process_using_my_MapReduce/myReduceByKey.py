"""
Develop myReduceByKey
*********************
- iterate through collection of tuples
- Group data by first element in the collection of tuples and apply the function using the argument passed.
  Argument should have the necessary arithmetic logic
- Retunr collection of tuples, where first element is unique and second element is aggregated result
"""

def myReduceByKey( coll_pair , fn):
    res_dict={}
    for e in coll_pair:
        if e[0] in res_dict:
            res_dict[e[0]]= fn(res_dict[e[0]], e[1])
        else:
            res_dict[e[0]]= e[1]
    return (list(res_dict.items()))




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


if __name__ == "__main__":

    from myFilter import myFilter
    from myMap import myMap
    from myReduce import myReduce

    #Read "Orders.txt" File into a list object
    orders=open('C:\\Users\\navaras2012\\Downloads\\Orders.txt').read().splitlines()
    #print(orders[:2])

    #Read "Order_items.txt" File into a list object
    order_items=open('C:\\Users\\navaras2012\\Downloads\\Order_Items.txt').read().splitlines()
    #print(order_items[:2])

    #(1) Use the function to get the count by date from orders

    map_date=myMap( orders , 
                    lambda o: ( o.split(',')[1][:10] , 1 ) )   # Map the records into to tuple - ( Date , 1) 
    #print(map_date[:2])
    order_count_by_date=myReduceByKey(map_date,
                                lambda x,y: x+y )
    print(f'{order_count_by_date[:5]=}')
    
    #(2) Use the function to get the revenue for each order id

    map_orderid_subtotal=myMap( order_items,
                                lambda oi: ( int(oi.split(',')[1]), float(oi.split(',')[4]) ) 
                              )                                                       
    # Map the records into to tuple - (order_id, subtotal)
    #print(map_orderid_subtotal[:2]) 
    revenue_per_order=myReduceByKey( map_orderid_subtotal,
                                     lambda x,y: round(x+y,2) 
                                   )
    print(f'{revenue_per_order[:5]=}')

    #(3) Use the function to get the revenue + order item count for each order id 

    map_orderid_subtotal_2=myMap( order_items,
                                  lambda oi: ( int(oi.split(',')[1]), ( float(oi.split(',')[4]), 1 ) ) 
                                ) 
    # Map the records into to tuple - (order_id, (subtotal,1))
    #print(map_orderid_subtotal[:2]) 
    revenue_per_order_2=myReduceByKey( map_orderid_subtotal_2,
                                       lambda x,y: ( round(x[0]+y[0],2), x[1]+y[1] )
                                     )
    print(f'{revenue_per_order_2[:5]=}')


