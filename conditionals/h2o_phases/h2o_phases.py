"""Temperature (°C)	Phase
Below 0	solid
0 to 100	liquid
Above 100	gas"""

temperature = float(input("Enter the temperature: "))

if temperature < 0:
    print("solid")
elif temperature == 0:
    print("solid or liquid")
elif temperature < 100:
    print("liquid")
elif temperature == 100:
    print("liquid or gas")
else:
    print("gas")