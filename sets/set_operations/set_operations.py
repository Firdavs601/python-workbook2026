def uniques(values: list) -> set:
    res = set()
    for value in values:
        res.add(value)
    return res

def union(set1: set, set2: set) -> set:
    res = set()
    for i in set1:
        res.add(i)
    for i in set2:
        res.add(i)
    return res


def intersection(set1: set, set2: set) -> set:
    res = set()
    for i in set1:
        if i in set2:
            res.add(i)
    return res

def is_subset(subset: set, superset: set) -> bool:
    for i in subset:
        if i not in superset:
            return False
    return True

def symmetric_diff(set1: set, set2: set) -> set:
    res = set()
    for i in set1:
        if i not in set2:
            res.add(i)
    for i in set2:
        if i not in set1:
            res.add(i)
    return res
    

if __name__ == "__main__":
    print(uniques([2, 3, 3, 5, 5, 5]))  # {2, 3, 5}
    print(union({2, 3, 5}, {5, 7, 11}))  # {2, 3, 5, 7, 11}
    print(intersection({2, 3, 5, 7}, {5, 7, 11, 13}))  # {5, 7}
    print(is_subset({2, 3}, {2, 3, 5, 7}))  # True
    print(is_subset({2, 11}, {2, 3, 5, 7}))  # False
    print(symmetric_diff({2, 3, 5}, {3, 5, 7}))  # {2, 7}