
total = 0
while True:
    a = input()
    if a == "":
        break
    total = total + float(a)
print(f"Total: ${total:.2f}") 
b = round(total * 100)
ostatok = b % 5
if ostatok < 2.5:
    b -= ostatok
    total = b / 100
    print(f"Cash payment: ${total:.2f}")
else:
    b += (5 - ostatok)
    total = b / 100
    print(f"Cash payment: ${total:.2f}") 