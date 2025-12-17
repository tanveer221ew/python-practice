
# num = 0
# while num == 0:
#     rand = input("Enter:")
#     if rand == "Exit":
#         break
while True:
    rand = input("Enter:").strip().lower() # strip() removes extra space in user input
    if rand == "exit":
        print("Program stopped")
        break