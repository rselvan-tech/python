import pandas as pd
orders_path="C:\\Users\\navaras2012\\Downloads\\Orders.txt"
orders_schema=[
"order_id",
"order_date",
"customer_id",
"order_status"
]

orders=pd.read_csv( orders_path,
                    delimiter=',',
                    header=None,
                    names=orders_schema
                  )
print(type(orders))
#print(orders[:10])

print(orders.head(10))

order_items_path='C:\\Users\\navaras2012\\Downloads\\Order_Items.txt'

order_items_schema=[
"order_item_id",
"order_item_order_id",
"order_item_product_id",
"order_item_quantity",
"order_item_subtotal",
"order_item_product_price"
]
order_items=pd.read_csv( order_items_path,
                         delimiter=',',
                         header=None,
                         names=order_items_schema
                       )
print(order_items[:10])

#Projection
#**********

#(1) Project order_date
print('****************************************(1) Project order_date****************************************************')
print(orders.order_date)
print(orders['order_date'])
print(type(orders.order_date))                                                 #Series         
print('******************************************************************************************************************')
#(2) Project fields from order_items
print('**************************************(2) Project fields from order_items******************************************')
print(order_items[['order_item_order_id','order_item_subtotal']])

print(type(order_items[['order_item_order_id','order_item_subtotal']]))        #DataFrame
print('******************************************************************************************************************')


#Filtering Data
#**************

#(3)Filter for order_item_order_id 2
print('***********************************(3)Filter for order_item_order_id 2**********************************************')

print(order_items[order_items.order_item_order_id == 2])        #Type-1

print(order_items.order_item_order_id == 2)                     #returns Series with True/False 

print(order_items[order_items['order_item_order_id'] == 2])     #Type-2

print(order_items.query('order_item_order_id == 2'))            #Type-3
print('******************************************************************************************************************')

#(4)Filter for order_item_order_id 2 and order_item_subtotal is b/w 150 and 250
print('****************************(4)Filter for order_item_order_id 2 and order_item_subtotal is b/w 150 and 250*********')
print( order_items[ (order_items.order_item_order_id == 2) &
                    ( (order_items.order_item_subtotal >= 150) &
                      (order_items.order_item_subtotal <= 250)
                    ) 
                  ]
     )                                                           #Type-1

print(order_items.query('order_item_order_id == 2 and order_item_subtotal >=150 and order_item_subtotal <=250'))   #Type-3

print(order_items.query('order_item_order_id == 2 and ' + 
                        'order_item_subtotal >=150 and '+ 
                        'order_item_subtotal <=250'))   #Type-3
print('******************************************************************************************************************')

#(5)Filter for orders placed on 2013 August 1st
print('****************************************(5)Filter for orders placed on 2013 August 1st*****************************')
print(orders[orders.order_date == '2013-08-01 00:00:00.0'])     #Type-1

print(orders[orders.order_date.str.startswith('2013-08-01')])     #Type-1

print(orders.query('order_date.str.startswith("2013-08-01")'))    #Type-3
print('******************************************************************************************************************')



#Aggregation(Global Aggregations)
#*******************

#(6)Getting number of records in the DataFrame
print('****************************************(6)Getting number of records in the DataFrame******************************')
print(orders.shape)         #(68883, 4)
print(type(orders.shape))   #Tuple

print(orders.shape[0])      #68883
print('******************************************************************************************************************')

#(7)Getting number of values(non np.NaN) in each atrribute in the DataFrame
print('********************(7)Getting number of values(non np.NaN) in each atrribute in the DataFrame*******************')
print(orders.count())
print(type(orders.count()))   #Series
#print(orders.count()[0])     #treating keys as positions is deprecated


print(orders.count()['order_id'])   #no of values in the order_id column
print('******************************************************************************************************************')

#(8)Getting basic statistics of numeric fileds of a DataFrame
print('***************************(8)Getting basic statistics of numeric fileds of a DataFrame***************************')
print(orders.describe())
print(order_items.describe())
print('******************************************************************************************************************')

#(9)Get revenue for a order_id 2 from order_items
print('****************************************(9)Get revenue for a order_id 2 from order_items**************************')
print(order_items[order_items.order_item_order_id==2])
print(order_items[order_items.order_item_order_id==2]['order_item_subtotal'])
print(order_items[order_items.order_item_order_id==2]['order_item_subtotal'].sum())
print('******************************************************************************************************************')

#Aggregation(By key aggregations)
#********************************

#(10)Getting number of orders per day
print('****************************************(10)Getting number of orders per day**************************************')
print(orders.groupby('order_date').count())   #DataFrame

print(orders.groupby('order_date')['order_date'].count())   #Series
print('******************************************************************************************************************')

#(11)Getting number of orders per sataus
print('****************************************(11)Getting number of orders per sataus***********************************')
print(orders.groupby('order_status').count())   #DataFrame

print(orders.groupby('order_status')['order_status'].count())   #Series
print('******************************************************************************************************************')

#(12)Compute revenue per order
print('****************************************(12)Compute revenue per order*********************************************')
print( order_items.groupby('order_item_order_id')['order_item_subtotal'].sum() )
print('******************************************************************************************************************')

#(13)agg
print('****************************************(13)agg*******************************************************************')
print( order_items.groupby('order_item_order_id')['order_item_subtotal'].agg(['sum','min','max','count']) )
print('******************************************************************************************************************')

#(14)Alias
print('****************************************(14)Alias****************************************************************')
print( order_items.groupby('order_item_order_id')['order_item_subtotal'].agg(['sum','min','max','count']).rename(columns={'count': 'item_count','sum':'revenue'}))

print(order_items.rename(columns={'order_item_order_id':'order_id'}))
print('******************************************************************************************************************')

#Writing to Files
#****************

#(15)write revenue per order into a csv file
print('**********************************(15)write revenue per order into a csv file**************************************')
print(order_items.groupby('order_item_order_id')['order_item_subtotal'].sum().to_csv()
print('******************************************************************************************************************')


#(15)write revenue per order into a json file
