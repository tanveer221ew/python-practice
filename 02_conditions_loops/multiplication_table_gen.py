# 3	Multiplication table generator.
num = int(input("Enter the number:"))
length = int(input("Enter the length of multiplication table:"))
counter = 0

while counter < length:
    counter += 1
    print(f"{num} * {counter} = {num*counter}")
    if counter == length:
        break
