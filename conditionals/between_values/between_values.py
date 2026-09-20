a = int(input())
b = int(input())
c = int(input())

if min(a, c) <= b <= max(a, c):
    print("between")
else:
    print("not between")