def binary_to_decimal():
    binary_str = input("Enter a binary number: ").strip()
    if not all(char in '01' for char in binary_str) or not binary_str:
        print("Invalid input. Please enter a valid binary number containing only 0 and 1.")
        return
    result = 0
    for digit in binary_str:
        result = result * 2
        result = result + int(digit)
    print(f"The decimal equivalent is {result}")
if __name__ == "__main__":
    binary_to_decimal()
