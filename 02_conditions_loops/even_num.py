#7.	Print all even numbers between 1–100
num = 0
even_num = 0
while num <=99:
    num+=1
    print(num)
    for digit in num:
        if digit % 2 == 0:
            print(digit)
        