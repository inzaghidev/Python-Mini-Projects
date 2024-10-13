def decimal_to_hexadecimal(number):
    integer_part = int(number)
    fractional_part = number - integer_part

    hex_integer = hex(integer_part)[2:]
    hex_fraction = decimal_fraction_to_hexadecimal(fractional_part)

    return hex_integer + "." + hex_fraction

def decimal_fraction_to_hexadecimal(fraction):
    hex_digits = "0123456789ABCDEF"
    hex_fraction = ""
    for i in range(10):
        fraction *= 16
        digit = int(fraction)
        hex_fraction += hex_digits[digit]
        fraction -= digit
    return hex_fraction

# Example usage:
decimal_number = 1234.5678
hexadecimal_number = decimal_to_hexadecimal(decimal_number)
print(hexadecimal_number)
