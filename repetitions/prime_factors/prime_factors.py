nums = int(input("Enter nums "))
if nums < 2:
    print("Error: Number must be 2 or greater")
else:
    factor = 2
    while factor <= nums:
        if nums % factor == 0:
            print(factor)
            nums //= factor
        else:
            factor += 1
    print(f"The prime factors of {nums} are:")