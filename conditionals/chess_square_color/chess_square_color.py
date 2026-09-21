square = input().strip()

file = ord(square[0]) - ord('a')
rank = int(square[1])

if (file + rank) % 2 == 1:
    print("black")
else:
    print("white")
