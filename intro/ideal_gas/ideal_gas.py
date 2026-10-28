p = int(input("Enter pressure (Pascals): "))
v = float(input("Enter volume (liters): "))
v /= 1000
t = int(input("Enter temperature (°C): "))
t += 273.15
r = 8.314
n = (p * v) / (r * t)
print(f"Amount of gas: {n:.2f} moles")