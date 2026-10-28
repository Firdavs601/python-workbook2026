sum = 0
count = 0
while True:
    num = int(input())
    if num == 0:
        break
    sum += num 
    count += 1
average = sum/count
print(f"The average is {average:.1f}")