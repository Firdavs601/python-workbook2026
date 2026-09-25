import random

def simulate_max_updates():
    first_val = random.randint(1, 100)
    print(first_val)
    
    current_max = first_val
    update_count = 0

    for _ in range(99):
        val = random.randint(1, 100)
        
        if val > current_max:
            current_max = val
            update_count += 1
            print(f"{val} <== Update")
        else:
            print(val)

    print(f"The maximum value found was {current_max}")
    print(f"The maximum value was updated {update_count} times")

if __name__ == "__main__":
    simulate_max_updates()
