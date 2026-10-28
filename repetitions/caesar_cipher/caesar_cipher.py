message = input()
shift = int(input())

result = []
for char in message:
    if char.isalpha():
        base = ord('A') if char.isupper() else ord('a')
        shifted_char = chr(base + (ord(char) - base + shift) % 26)
        result.append(shifted_char)
    else:
        result.append(char)
print("".join(result))