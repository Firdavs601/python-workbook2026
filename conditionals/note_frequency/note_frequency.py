note = input().strip().upper()

base_frequencies = {
    "C": 261.63,
    "D": 293.66,
    "E": 329.63,
    "F": 349.23,
    "G": 392.00,
    "A": 440.00,
    "B": 493.88
}

letter = note[0]

if letter not in base_frequencies:
    print("Invalid note")
else:
    octave = int(note[1:])
    base_frequency = base_frequencies[letter]

    frequency = base_frequency / (2 ** (4 - octave))

    print(f"{frequency:.2f}")
