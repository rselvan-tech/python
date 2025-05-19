#Immutable data types = int, float, str, tuple 
#Mutable data type= list, set, dict
name='Marry'
id1=id(name)
name='Lena'
id2=id(name)     #id2 will have new address , since name value changed beacuase 'str' is immutable
print(id1==id2)

name2=name
print(name2 is name) # 'is' identity operator , it does not compare value instead it compares the memory address refered by the variable
