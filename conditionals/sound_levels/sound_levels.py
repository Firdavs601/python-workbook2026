"""Noise	Decibel Level
Quiet Room	40 dB
Alarm Clock	70 dB
Gas Lawnmower	106 dB
Jackhammer	130 dB
"""







level = int(input("Enter the sound level in decibels: "))

if level == 40:
	print("Quiet Room")
elif level == 70:
	print("Alarm Clock")
elif level == 106:
	print("Gas Lawnmower")
elif level == 130:
	print("Jackhammer")
elif level < 40:
	print("Quieter than Quiet Room")
elif level < 70:
	print("Between Quiet Room and Alarm Clock")
elif level < 106:
	print("Between Alarm Clock and Gas Lawnmower")
elif level < 130:
	print("Between Gas Lawnmower and Jackhammer")
else:
	print("Louder than Jackhammer")

