# 1.	Function to calculate factorial of a number.
def fact(num):
    counter = 1
    result = 1
    while counter <= num:
        result = counter*result
        counter+=1
    print(f"Factorial of {num} is {result}")


# fact(3)