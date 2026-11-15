def remove_duplicate_letters(text: str) -> str:
    s = set()
    result = ""

    for letter in text:
        if letter not in s:
            result += letter
            s.add(letter)
    return result




if __name__ == "__main__":
    print(remove_duplicate_letters("hello"))  # "helo"
    print(remove_duplicate_letters("mississippi"))  # "misp"
    print(remove_duplicate_letters("abcabc"))  # "abc"
    print(remove_duplicate_letters("AaAaBb"))  # "AaBb"
    print(remove_duplicate_letters(""))  # ""
