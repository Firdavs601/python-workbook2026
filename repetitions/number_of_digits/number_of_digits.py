number_str = input()
number = abs(int(number_str))
if number == 0:
    count = 1
else:
    count = 0
    while number > 0:
        count += 1
        number = number // 10
print(count)