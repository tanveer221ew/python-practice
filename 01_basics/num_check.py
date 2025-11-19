# 8.	Check if a number is positive, negative, or zero.
user_input = int(input("Enter the number:"))
if user_input == 0:
    print("Zero")
elif user_input % 2 == 0:
    print("Even")
else:
    print("Odd")