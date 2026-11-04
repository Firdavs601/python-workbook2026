def to3x3matrix(string: str) -> list[list[int]]:
    nums = [int(x) for x in string.split()]
    return [nums[i : i + 3 ] for i in range(0 , len(nums), 3)]

if __name__ == "__main__":
    # Test your function
    matrix = to3x3matrix("2 3 5 7 11 13 17 19 23")
    for row in matrix:
        print(row)
    # Output:
    # [2, 3, 5]
    # [7, 11, 13]
    # [17, 19, 23]
