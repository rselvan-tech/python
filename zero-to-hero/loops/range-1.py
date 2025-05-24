r=range(2,10)
print(type(r))                 #<class 'range'>
print(r)                       #range(2, 10)
print(list(r))                 #[2, 3, 4, 5, 6, 7, 8, 9]

print(list(range(10)))         #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(range(0,11,2)))     #[0, 2, 4, 6, 8, 10]

print(list(range(0,40,7)))     #[0, 7, 14, 21, 28, 35]

s=sum(range(1,1001))
print(f'Sum = {s}')            #Sum = 500500

print(list(range(-10,20,5)))   #[-10, -5, 0, 5, 10, 15]

print(list(range(100,-50,-10))) #[100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, -10, -20, -30, -40]

print(list(range(-10,99,3)))

print(list(range(99,-4,-2)))