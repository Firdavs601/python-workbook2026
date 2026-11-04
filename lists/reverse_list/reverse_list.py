def reverse_list(string: str) -> list[int]:
    if string == "":
        return []
    else:
        parts = string.split()
        res = []
        for i in parts:
            res.append(int(i))
        return res[::-1]