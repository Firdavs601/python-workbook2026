syl=int(input("Enter num: "))

year  = {
    1: "Freshman",
	2: "Sophomore ",
	3: "Junior",
	4: "Senior",
}

if syl in year :
	print(year[syl])
else:
	print("Invalid year")