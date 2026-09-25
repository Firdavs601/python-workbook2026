line = input()
if line != "":
    current_value = int(line)
    min_value = current_value
    max_value = current_value
    while True:
        line = input()
        if line == "":
            break
        current_value = int(line)
        if current_value < min_value:
            min_value = current_value
        if current_value > max_value:
            max_value = current_value
    print(f"Minimum: {min_value}")
    print(f"Maximum: {max_value}")