current_streak = 0
max_streak = 0

while True:
    line = input()
    if line == "":
        break
    result = int(line)
    if result == 1:
        current_streak += 1
    else:
        if current_streak > max_streak:
            max_streak = current_streak
        current_streak = 0
if current_streak > max_streak:
    max_streak = current_streak
print(f"Maximum streak: {max_streak}")
