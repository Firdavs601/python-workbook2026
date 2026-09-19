#subtotal   45.50
#discount    2.73
#total      42.77


 #f"{label:<10}{value:>6.2f}"

a=float(input("Enter the first number: "))
b=float(input("Enter the second number: "))
subtotal=a*b
print(f"subtotal{subtotal:>6.2f}")
c=float(input("Enter the discount rate (%): "))
discount=subtotal*c/100
print(f"discount{discount:>6.2f}")
total=subtotal-discount
print(f"total{total:>6.2f}")

