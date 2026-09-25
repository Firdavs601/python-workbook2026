def caesar_cipher():
    message = input("Enter a message: ")
    try:
        shift = int(input("Enter shift amount: "))
    except ValueError:
        print("Invalid shift amount. Please enter an integer.")
        return

    result = ""

    for char in message:
        if char.isupper():
            start = ord('A')
            position = ord(char) - start
            new_position = (position + shift) % 26
            result += chr(start + new_position)
        elif char.islower():
            start = ord('a')
            position = ord(char) - start
            new_position = (position + shift) % 26
            result += chr(start + new_position)
        else:
            result += char

    print(result)

if __name__ == "__main__":
    caesar_cipher()
