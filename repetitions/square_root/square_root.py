x = int(input("Enter number: "))
guess = x / 2
while 1e-12 < abs(guess * guess - x):
    guess = (guess + x / guess) / 2
if abs(guess - round(guess)) < 1e-12:
    print(float(round(guess)))
else:
    print(guess)
