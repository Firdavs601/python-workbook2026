import math


lat1 = float(input("Enter latitude of first point: "))
lon1 = float(input("Enter longitude of first point: "))
lat2 = float(input("Enter latitude of second point: "))
lon2 = float(input("Enter longitude of second point: "))

lat1 *= 0.0174533
lon1 *= 0.0174533
lat2 *= 0.0174533
lon2 *= 0.0174533

distance = 6371.01 * math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2))

print(f"Distance: {distance:.2f} km")