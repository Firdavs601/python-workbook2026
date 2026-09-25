total_cost = 0.0

while True:
    line = input()
    if line == "":
        break
    age = int(line)
    if age <= 2:
        total_cost += 0.00
    elif 3 <= age <= 12:
        total_cost += 14.00
    elif age >= 65:
        total_cost += 18.00
    else:
        total_cost += 23.00
print(f"${total_cost:.2f}")