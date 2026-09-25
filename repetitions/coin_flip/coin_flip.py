import random

flips_history = []

for _ in range(10):
    flips = []
    
    first_flip = random.choice(['H', 'T'])
    flips.append(first_flip)
    
    consecutive_count = 1
    previous_flip = first_flip
    
    while consecutive_count < 3:
        new_flip = random.choice(['H', 'T'])
        flips.append(new_flip)
        
        if new_flip == previous_flip:
            consecutive_count += 1
        else:
            consecutive_count = 1
            
        previous_flip = new_flip
        
    total_flips = len(flips)
    flips_history.append(total_flips)
    print(f"{' '.join(flips)} ({total_flips} flips)")

average_flips = sum(flips_history) / len(flips_history)
print(f"\nOn average, {average_flips:.1f} flips were needed.")
