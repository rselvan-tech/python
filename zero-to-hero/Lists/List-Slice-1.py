print('#'*10+' LIST SLICING '+'#'*10)

nums1=[1,2,3,4,5,6,7]
print(nums1)             #[1, 2, 3, 4, 5, 6, 7]

nums2=nums1[1:4]
print(nums2)             #[2, 3, 4]

print(nums1[3:])         #[4, 5, 6, 7]
print(nums1[:4])         #[1, 2, 3, 4]
print(nums1[::2])        #[1, 3, 5, 7]

print(nums1[4:1:-2])     #[5, 3]

print(nums1[1:100])      #[2, 3, 4, 5, 6, 7]
#print(nums1[100])       #IndexError: list index out of range

my_str="python"
print(my_str[1:100])      #ython
#print(my_str[100])       #IndexError: string index out of range


print('#'*10+' LIST Iteration '+'#'*10)

ip_list=['12.34.56.7','192.169.3.4','12.45.45.32']

for ip in ip_list:
    print(f'Connecting to {ip}')

print('12.34.56.7' in ip_list)      #True
