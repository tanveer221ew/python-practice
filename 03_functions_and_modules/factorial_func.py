# 1.	Function to calculate factorial of a number.
def fact(num):
    counter = 0
    result = 1
    while counter < num:
        counter+=1
        result = result*counter
    return result

print(fact(3))
