def decimal_to_hexadecimal(decimal):
    hex_digits = "0123456789ABCDEF"
    hexadecimal = ""
    while decimal > 0:
        quotient = decimal // 16
        remainder = decimal % 16
        hexadecimal += hex_digits[remainder]
        decimal = quotient
    return hexadecimal[::-1]  # reverse the string

# Example usage:
decimal_number = 1234
hexadecimal_number = decimal_to_hexadecimal(decimal_number)
print(hexadecimal_number)
