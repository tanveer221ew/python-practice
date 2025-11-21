# 4.	Count vowels and consonants in a string.
str = str(input("Enter a string"))
vowels = 0
consonants = 0
for char in str:
    if char.isalpha():
        if char.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1


print(f"Number of vowels are {vowels}")
print(f"Number of consonants are {consonants} ")
