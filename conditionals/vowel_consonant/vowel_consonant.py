letter = input("Enter letter ")
if letter in ("AaEeUuIiOo"):
    print("vowel")
elif letter in ("Yy"):
    print("sometimes vowel, sometimes consonant")
else:
    print("consonant")