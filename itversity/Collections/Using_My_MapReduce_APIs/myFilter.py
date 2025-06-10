"""
Develop myFilter
****************
- Iterate Thorugh elements
- Apply the condition using the argument passed.we might pass named or lambda function
- Return the colletion with all the elements satisfying the condition
"""

def myFilter(order_coll, fn):
    result=[]

    for o in order_coll:
        if fn(o):
            result.append(o)
    return result


'''
Orders File
================
- order_id
- order_date
- customer_id
- order_status
'''

if __name__ == "__main__":
    #Read "Orders.txt" File into a list object
    orders=open('C:\\Users\\navaras2012\\Downloads\\Orders.txt').read().splitlines()
    #print(orders[:2])

    #(1)Get Orders placed by customer id 12431
    orders_by_customer_id = myFilter(orders, lambda n: int(n.split(',')[2])== 12431 )
    print(f'{orders_by_customer_id=}')

    """
    #Get Orders placed by customer id 11599
    orders_by_customer_id = myFilter(orders, lambda n: int(n.split(',')[2])== 11599 )
    print(f'{orders_by_customer_id=}')
    """

    #(2)Get Orders placed by customer id 12431 in the month of 2014 January
    #orders_by_customer = myFilter(orders, lambda n: (int(n.split(',')[2])== 12431) and (n.split(',')[1][:7]=='2014-01')  )
    orders_by_customer_month = myFilter(orders, lambda n: (int(n.split(',')[2])== 12431) 
                                                           and (n.split(',')[1].startswith('2014-01'))
                                       )
    print(f'{orders_by_customer_month=}')

    #(3)Get Orders placed by customer id 12431 in the month of 2014 January and status=PENDING_PAYMENT
    orders_by_customer_status = myFilter(orders, lambda n: (int(n.split(',')[2])== 12431) 
                                                            and (n.split(',')[1].startswith('2014-01')) 
                                                            and (n.split(',')[3]== 'PENDING_PAYMENT') 
                                        )
    print(f'{orders_by_customer_status=}')


