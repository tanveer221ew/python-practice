# 8.	Find factorial using while loop.

num = int(input("Enter the you number"))
result = 1
counter = 1
while counter <= num:  
    result = counter*result
    counter+=1
print(f'The factorial of {num} is {result}')