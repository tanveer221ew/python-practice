# 10.	Print all Fibonacci numbers up to 100.
# Fibonacci numbers: 0,1,1,2,3,5,8,13,21, ... 

a = 0
b = 1
print(a)
while b <= 100:
    print(b)
    next_num = a + b
    a = b
    b = next_num
