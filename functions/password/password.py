import random
import string

def password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    result = ""
    for _ in range(length):
        result += random.choice(chars)
    return result
