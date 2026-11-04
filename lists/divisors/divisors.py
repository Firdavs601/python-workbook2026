def divisors(n: int) -> list[int]:
    res = []
    for i in range(1, n + 1):
        if n % i == 0:
            res.append(i)
    return res