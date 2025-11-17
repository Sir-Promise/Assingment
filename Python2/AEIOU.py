letter = input("Enter a letter: ").lower()

if letter.isalpha() and len(letter) == 1:
if letter in 'aeiou':
print("Vowel")
else:
print("consonant")
else:
print("Invalid input")
