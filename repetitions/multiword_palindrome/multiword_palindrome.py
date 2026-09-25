import string

def check_palindrome():
    original_string = input("Enter a phrase: ")
    cleaned_string = ""
    for char in original_string.lower():
        if char != " " and char not in string.punctuation:
            cleaned_string += char
    if not cleaned_string:
        print("Please enter a phrase containing alphanumeric characters.")
        return
    is_palindrome = True
    length = len(cleaned_string)
    
    for i in range(length // 2):
        if cleaned_string[i] != cleaned_string[-(i + 1)]:
            is_palindrome = False
            break  
    if is_palindrome:
        print(f"`{original_string}` is a palindrome")
    else:
        print(f"`{original_string}` is not a palindrome")
if __name__ == "__main__":
    check_palindrome()
