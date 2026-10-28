pi = 3.0
print(f"Approximation 1: {pi}")

n = 2

for i in range(2, 16):
    denominator = n * (n + 1) * (n + 2)
    fraction = 4.0 / denominator
    
    if i % 2 == 0:
        pi = pi + fraction
    else:
        pi = pi - fraction
        
    print(f"Approximation {i}: {pi}")
    n = n + 2
