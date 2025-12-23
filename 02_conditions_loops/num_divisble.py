# Check if a number is divisible by 3 and 5.
num = int(input("Enter a number to check if its divisble by 3 and 5:"))
if num % 3 == 0 and num % 5 == 0:
    print("It is divisble by 3 and 5")
else:
    print("Not divisble")