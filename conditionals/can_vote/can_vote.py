#If age >= 18: can vote
#If age < 18: cannot vote

age=int(input("Enter your age: "))
if age >= 18:
    print ("can vote")
elif age<18:
    print("cannot vote")
else:
    print("You can vote ")
