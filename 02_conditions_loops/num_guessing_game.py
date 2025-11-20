# 2.	Number guessing game (computer picks random number, user guesses).
import random

num = random.randint(1, 10)
guesses = 5
won = False
while guesses > 0:
    user_input = int(input(f"Enter your guess between 1-10 you have {guesses} remaining"))
    if user_input == num:
        print("You guessed it right")
        won = True
        break
    if user_input < num:
        guesses -= 1
        print("Its greater")
        print(f"You have {guesses} guesses remaining")
    elif user_input > num:
        guesses -= 1
        print("Its lesser")
        print(f"You have {guesses} guesses remaining")

if won == False:
    print("You lost, the number was", num)