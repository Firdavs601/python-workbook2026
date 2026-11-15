def is_isogram(text: str) -> bool:

    seen = set()

    for letter in text.lower():
        if letter in "abcdefghijklmnopqrstuvwxyz":
            if letter in seen:
                return False
            seen.add(letter)

    return True

if __name__ == "__main__":
    print(is_isogram("lumberjacks"))  # True
    print(is_isogram("isograms"))  # False
    print(is_isogram("Alphabet"))  # False
    print(is_isogram("thumbscrew-japingly"))  # True
    print(is_isogram("Emily Jung Schwartzkopf"))  # True
    print(is_isogram(""))  # True
