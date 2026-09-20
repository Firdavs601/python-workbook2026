# Input a 3-digit number
n = int(input("enter num: "))

# Extract digits
A = n // 100
B = (n // 10) % 10
C = n % 10

# Check if the first digit equals the last digit
if A == C:
    print("palindrome")
else:
    print("not palindrome")
