def longest_consecutive(numbers: list) -> int:
    numbers = sorted(set(numbers))
    if not numbers:
        return 0

    cur = 1
    long = 1

    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i - 1] + 1:
            cur += 1
        else:
            cur = 1
        long = max(long, cur)
        
    return long

            


if __name__ == "__main__":
    print(longest_consecutive([100, 4, 200, 1, 3, 2]))  # 4 (sequence: 1,2,3,4)
    print(longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9 (sequence: 0-8)
    print(longest_consecutive([1, 2, 0, 1]))  # 3 (sequence: 0,1,2)
    print(longest_consecutive([]))  # 0
    print(longest_consecutive([5]))  # 1
    print(longest_consecutive([1, 3, 5, 7]))  # 1 (no consecutive numbers)
