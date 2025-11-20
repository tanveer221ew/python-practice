# Ask the user to input two numbers and divide them.
# Use try-except to handle division by zero and invalid input.
# Print "Error! Cannot divide." if an error occurs.

num_1 = int(input("Enter first number:"))
num_2 = int(input("Enter second number:"))

try:
    print(num_1/num_2)
except:
    print("Error cannot divide by zero")
# print(num_1/num_2)