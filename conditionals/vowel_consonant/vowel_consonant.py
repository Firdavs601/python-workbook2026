#If letter is 'y': display "sometimes vowel, sometimes consonant"
#If letter is 'a', 'e', 'i', 'o', 'u' (case-insensitive): display "vowel"
#If the letter is any other alphabetic character: display "consonant"

letter1 = input("Enter letter:").strip()

if letter1.lower() == "y":
	print("sometimes vowel, sometimes consonant")
elif letter1.lower() in ("a", "e", "i", "o", "u"):
	print("vowel")
elif letter1.isalpha():
	print("consonant")
