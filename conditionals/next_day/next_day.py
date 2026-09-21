year = int(input())
month = int(input())
day = int(input())

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else:
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day += 1

if day > days[month - 1]:
    day = 1
    month += 1

if month > 12:
    month = 1
    year += 1

print(f"{year:04d}-{month:02d}-{day:02d}")