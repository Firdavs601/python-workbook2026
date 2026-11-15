vowels = set("aeiou")

def vowels_in(word):
    return sorted(vowels & set(word.lower()))

def missing_vowels(word):
    return sorted(vowels - set(word.lower()))
