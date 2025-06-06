db={'host':'abc',
    'db_name':'reliable_db'
    }
print(db)               #{'host': 'abc', 'db_name': 'reliable_db'}

#Dict Keys
print(db.keys())           #dict_keys(['host', 'db_name'])
print(set(db.keys()))      #{'host', 'db_name'}              <= Set of Keys
print(list((db.keys())))   #['host', 'db_name']              <= List of Keys


#Dict Values

print(db.items())          #dict_items([('host', 'abc'), ('db_name', 'reliable_db')])  
print(set(db.items()))     #{('host', 'abc'), ('db_name', 'reliable_db')}             <= Set of tuples           
print(list(db.items()))    #[('host', 'abc'), ('db_name', 'reliable_db')]             <= List of tuples

print(db.values())          #dict_values(['abc', 'reliable_db'])
print(set(db.values()))     #{'reliable_db', 'abc'}                <= Set of value strings          
print(list(db.values()))    #['abc', 'reliable_db']                <= List of value strings


#Access Values
db['host']='xyz'
print(db)
print(db['host'])
print(db.get('db_name'))

#Check Key Exist
print( 'host' in db)


#Check value Exist
print( 'abc' in db.values())

#Remove elements

print(db.pop('host'))
print(db)

print(db.popitem())
print(db)

help(dict.get)



