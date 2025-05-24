nums = [1, 2, 4, 7, 8]
s = 0
for n in nums:
    s += n
    if s >=4:
        break
print(f's={s}')