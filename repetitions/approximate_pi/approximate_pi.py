pi_approx = 3.0
print(f"Approximation 1: {pi_approx}")

sign = 1
for i in range(2, 16):
    n = (i - 1) * 2
    denominator = n * (n + 1) * (n + 2)
    pi_approx += sign * (4.0 / denominator)
    print(f"Approximation {i}: {pi_approx}")
    sign *= -1

