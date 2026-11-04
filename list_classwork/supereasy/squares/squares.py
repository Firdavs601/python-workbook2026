def squares(n):
    result = []
    for i in range(1 , n + 1):
        result.append(i ** 2)
    return result

def list_sum(nums):
    total = 0
    for i in nums:
        total += i
    return total