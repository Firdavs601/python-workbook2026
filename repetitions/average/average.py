total_sum = 0
count = 0
value = float(input())
while value != 0:
    total_sum += value
    count += 1
    value = float(input())
if count > 0:
    average = total_sum / count
    print(f"The average is {average:.1f}")

