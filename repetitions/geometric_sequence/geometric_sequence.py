
start = float(input())

ratio = float(input())

count = int(input())

current_term = start

for _ in range(count):
    print(f"{current_term:.9g}")
    current_term *= ratio
