letters_volwes = ["a", "e", "i", "o", "u"]
letter = input("Enter letter: ")
if letter in letters_volwes:
    print("This letter is volwes!")
elif letter == "y":
    print("This letter is both a vowel and a consonant")
else:
    print("This letter is consonant!")