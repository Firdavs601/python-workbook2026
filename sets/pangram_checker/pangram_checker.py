def is_pangram(text: str) -> bool:
    alfavit = "abcdefghijklmnopqrstuvwxyz"
    text = text.lower()
    for i in alfavit:
        if i not in text:
            return False
    return True


if __name__ == "__main__":
    print(is_pangram("The quick brown fox jumps over the lazy dog"))  # True
    print(is_pangram("Pack my box with five dozen liquor jugs"))  # True
    print(is_pangram("Hello World"))  # False
    print(is_pangram("abcdefghijklmnopqrstuvwxyz"))  # True
    print(is_pangram("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))  # True
