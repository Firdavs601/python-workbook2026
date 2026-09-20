"""magnitude < 2.0	Micro
2.0 <= magnitude < 3.0	Very Minor
3.0 <= magnitude < 4.0	Minor
4.0 <= magnitude < 5.0	Light
5.0 <= magnitude < 6.0	Moderate
6.0 <= magnitude < 7.0	Strong
7.0 <= magnitude < 8.0	Major
8.0 <= magnitude < 10.0	Great
magnitude >= 10.0	Meteoric
"""

magnitude = float(input("Enter the magnitude: "))

if magnitude < 2.0:
    print("Micro")
elif magnitude < 3.0:
    print("Very Minor")
elif magnitude < 4.0:
    print("Minor")
elif magnitude < 5.0:
    print("Light")
elif magnitude < 6.0:
    print("Moderate")
elif magnitude < 7.0:
    print("Strong")
elif magnitude < 8.0:
    print("Major")
elif magnitude < 10.0:
    print("Great")
else:
    print("Meteoric")

