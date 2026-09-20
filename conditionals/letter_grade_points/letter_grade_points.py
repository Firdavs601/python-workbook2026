"""A+	4.0
A	4.0
A-	3.7
B+	3.3
B	3.0
B-	2.7
C+	2.3
C	2.0
C-	1.7
D+	1.3
D	1.0
F	0.0"""


grade = input("Enter your grade: ").strip().upper()

if grade == "A+" or grade == "A":
	points = 4.0
elif grade == "A-":
	points = 3.7
elif grade == "B+":
	points = 3.3
elif grade == "B":
	points = 3.0
elif grade == "B-":
	points = 2.7
elif grade == "C+":
	points = 2.3
elif grade == "C":
	points = 2.0
elif grade == "C-":
	points = 1.7
elif grade == "D+":
	points = 1.3
elif grade == "D":
	points = 1.0
elif grade == "F":
	points = 0.0
else:
	points = None

if points is None:
	print("Invalid grade")
else:
	print(points)