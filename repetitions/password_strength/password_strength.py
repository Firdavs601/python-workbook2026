def check_password_strength():
    password = input("Enter a password to evaluate: ")
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    has_length = len(password) >= 8
    special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True
    criteria_met = sum([has_upper, has_lower, has_digit, has_special, has_length])
    strength_levels = {
        1: "Very Weak",
        2: "Weak",
        3: "Medium",
        4: "Strong",
        5: "Very Strong"
    }
    if criteria_met in strength_levels:
        print(strength_levels[criteria_met])
    else:
        print("Very Weak")
if __name__ == "__main__":
    check_password_strength()
