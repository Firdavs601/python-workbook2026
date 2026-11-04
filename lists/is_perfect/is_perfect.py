def is_perfect(n: int) -> bool:
    res = []
    for i in range(1, n + 1):
        if n % i == 0:
            res.append(i)
    last_divisors = res[:-1]
    if sum(last_divisors) == n:
        return True
    else:
        return False