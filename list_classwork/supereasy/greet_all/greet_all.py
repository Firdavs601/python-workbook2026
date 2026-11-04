def greet_all(names):
    result=[]
    for name in names:
        result.append(f"Hello, {name}!")
    return result
def count_long_names(names):
    count = 0
    for i in names:
        if 4 < len(i):
            count += 1
    return count