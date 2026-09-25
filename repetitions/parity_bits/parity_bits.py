while True:
    line = input()
    if line == "":
        break
    if len(line) != 8:
        print("Error: Input must be exactly 8 bits.")
        continue
    ones_count = line.count('1')
    if ones_count % 2 != 0:
        parity_bit = 1
    else:
        parity_bit = 0
    print(f"Parity bit: {parity_bit}")
