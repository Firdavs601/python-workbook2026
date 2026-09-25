number_str = input()
number = abs(int(number_str))
digit_sum = 0
while number > 0:
    digit_sum += number % 10
    number = number // 10
print(digit_sum)
