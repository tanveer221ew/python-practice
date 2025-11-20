# 1.	Simple calculator using if-else statements.
num_one = int(input("Enter the first number:"))
num_two = int(input("Enter the second number:"))
operator = input("Enter the operation you want to perform(+, -, *, /):")

if operator == "+":
    print(num_one+num_two)
elif operator == "-":
    print(num_one-num_two)
elif operator == "*":
    print(num_one*num_two)
elif operator == "/":
    print(num_one/num_two)
else:
    print("Enter a valid Operator")