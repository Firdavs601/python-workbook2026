import random
maximum = random.randint(1, 100)
updates = 0
print(maximum)
for _ in range(99):
    number = random.randint(1, 100)
    if number > maximum:
        maximum = number
        updates += 1
        print(f"{number} <== Update")
    else:
        print(number)
print(f"The maximum value found was {maximum}")
print(f"The maximum value was updated {updates} times")
