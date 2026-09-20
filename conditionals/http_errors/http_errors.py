"""Range	Category
100-199	Informational
200-299	Success
300-399	Redirection
400-499	Client Error
500-599	Server Error
"""

a = int(input("Enter HTTP status code: "))

if 100 <= a <= 199:
	b = "Informational"
elif 200 <= a <= 299:
	b = "Success"
elif 300 <= a <= 399:
	b = "Redirection"
elif 400 <= a <= 499:
	b = "Client Error"
elif 500 <= a <= 599:
	b = "Server Error"
else:
	b = "Unknown status code"

print(b)