# Print multiplication table of a number.
user_input = int(input("Enter number:"))
num = 1
while num <= 10:
    print(f"{user_input} * {num} = {user_input*num}")
    num+=1