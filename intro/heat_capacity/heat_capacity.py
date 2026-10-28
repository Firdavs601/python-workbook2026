C = 4.186
m = int(input("Enter volume of water (liters): "))
temperature = int(input("Enter temperature change (°C): "))
m *= 1000
energy = m * C *temperature
kWh = energy / 3600000
cost = kWh * 0.04
print(f"Energy required: {kWh:.2f} kWh")
print(f"Cost to heat water: ${round(cost, 2)}")