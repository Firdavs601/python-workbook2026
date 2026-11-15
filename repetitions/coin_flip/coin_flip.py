import random
total = 0
for simulation in range(10):
    count = 0 
    streak = 0
    previous = ""
    while streak < 3:
        count += 1
        flip = random.choice("HT")
        print(flip, end=" ")
        if flip == previous:
            streak += 1
            previous = flip
        else:
            streak = 1
            previous = flip
    total += count        
    print(f"({count} flips)")
print(f"On average, {total / 10} flips were needed.")