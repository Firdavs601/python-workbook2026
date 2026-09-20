
a = int (input("Enter the length of the first side: "))
b = int (input("Enter the length of the second side: "))
c = int (input("Enter the length of the third side: "))


if a == b and b == c and c == a:
    print ("equilateral")
elif a == b or b == c or a == c:
    print("isosceles")
else:
    print ("scalene")
