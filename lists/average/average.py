def average(numbers: list[int]) -> float:
    sum_nums = 0
    for i in numbers:
        sum_nums += i
    return sum_nums / len(numbers)


if __name__ == "__main__":
    # Test your function
    print(average([2, 3, 5, 7, 11]))  # 5.6
    print(average([10, 20, 30]))      # 20.0
    print(average([5]))               # 5.0
