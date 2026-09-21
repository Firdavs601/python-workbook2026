a = input().lower()
b = input().lower()

if a == "gas":
    if b == "gas":
        print("No transition")
    elif b == "liquid":
        print("condensation")
    elif b == "plasma":
        print("ionization")
    elif b == "solid":
        print("deposition")

elif a == "liquid":
    if b == "gas":
        print("vaporization")
    elif b == "liquid":
        print("No transition")
    elif b == "plasma":
        print("Cannot transition directly")
    elif b == "solid":
        print("freezing")

elif a == "solid":
    if b == "gas":
        print("sublimation")
    elif b == "liquid":
        print("melting")
    elif b == "plasma":
        print("Cannot transition directly")
    elif b == "solid":
        print("No transition")

elif a == "plasma":
    if b == "gas":
        print("recombination")
    elif b == "liquid":
        print("Cannot transition directly")
    elif b == "plasma":
        print("No transition")
    elif b == "solid":
        print("Cannot transition directly")
