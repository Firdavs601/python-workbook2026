password =input("Enter password")
has_upper = False
has_digit = False 
has_special = False 
has_length = False
has_lower = False
for char in password:
    if char.isupper():
        has_upper = True
    if char.islower():
        has_lower = True
    if char.isdigit():
        has_digit = True
    if char in "!@#$%^&*()_+-=[]{}|;:,.<>?":
        has_special = True
if len(password) >= 8:
    has_length = True
score = 0
if has_upper:
    score += 1
if has_special:
    score += 1
if has_length:
    score += 1
if has_lower:
    score += 1
if has_digit:
    score += 1
if score == 1:
    print("Very Weak")
elif score == 2:
    print("Weak")
elif score == 3:
    print(	"Medium")
elif score == 4:
    print("Strong")
elif score == 5:
    print("Very Strong")

