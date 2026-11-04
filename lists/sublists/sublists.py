def sublists(l: list) -> list[list]:
    res = [[]]
    
    for i in range(0,len(l)):
        for j in range(i + 1, len(l) + 1):
            res.append(l[i:j])
    return res












if __name__ == "__main__":
    # Test your function
    print(sublists([2, 3, 5]))
    # [[], [2], [3], [5], [2, 3], [3, 5], [2, 3, 5]]
