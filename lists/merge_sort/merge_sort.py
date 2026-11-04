def merge_sort(list1: list[int], list2: list[int]) -> list[int]:
    res = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            res.append(list1[i])
            i += 1
        else:
            res.append(list2[j])
            j += 1
    res.extend(list1[i:])
    res.extend(list2[j:])
    return res

if __name__ == "__main__":
    # Test your function
    print(merge_sort([2, 5, 11], [3, 7, 13]))  # [2, 3, 5, 7, 11, 13]
    print(merge_sort([2, 3], [5, 7]))          # [2, 3, 5, 7]
