# 6.	Count total characters and words from user input.
user_input = str(input("Enter you text:"))
no_of_words = len(user_input.split(sep=None))
no_of_chars = len(user_input.replace(" ", ""))

print(f"No characters {no_of_chars}\nNo of words {no_of_words}")
