# 9.	Sum of digits of a number.
num = int(input("Enter a number:"))
sum = 0
for digit in str(num):
    sum += num%10
    num //= 10
print(sum)
