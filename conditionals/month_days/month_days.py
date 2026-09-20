"""January	31
February	28 or 29
March	31
April	30
May	31
June	30
July	31
August	31
September	30
October	31
November	30
December	31"""


month = input("Enter month: ")


moth1 = {
    "January": 31,
    "february": '28 or 29',
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "DECEMBER": 31,
    "xyz": "Invalid month",
    "": "Invalid month",
    "jan": "Invalid month"
}  


if month in moth1:
    print(moth1[month])
else:
    print("Invalid month")