"""
Develop myMap
****************
- Iterate Thorugh elements
- Apply the transformation logic using the aregument passed
- Return the colletion with all the elements which are transformed based on the logic passed
"""

def myMap(coll,fn):
    res_coll=[]

    for i in coll:
        res_coll.append(fn(i))
    
    return res_coll



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

    #(1)reate a list for range b/w 1 to 9 and return square of each number
    square_list=myMap(list(range(0,10)),lambda n: n*n)
    print(f'{square_list=}')

    #(2)use orders and extract order_dates.Also apply set and get unique dates
    unique_dates=set(myMap(orders, lambda o: o.split(',')[1]))

    print(f'{unique_dates=}')
    print(len(unique_dates))

    #(3)use orders and extract order_id as well order_date from each element in the form of a tuple.Make sure that order_id is of type int
    order_id_date=myMap(orders, lambda o: ( int(o.split(',')[0]) , o.split(',')[1]))
    print(f'{order_id_date}')

