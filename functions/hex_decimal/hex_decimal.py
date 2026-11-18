def hex_decimal(hex_str):
    hex_chars = "0123456789abcdef"
    decimal_value = 0
    for char in hex_str.lower():
        digit_value = hex_chars.index(char)
        decimal_value = decimal_value * 16 + digit_value
    return decimal_value