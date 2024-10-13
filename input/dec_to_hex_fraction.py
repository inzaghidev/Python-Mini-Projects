def decimal_fraction_to_hexadecimal(decimal_fraction):
    hex_digits = "0123456789ABCDEF"
    hexadecimal = ""
    for i in range(10):  # convert up to n digits after the decimal point
        decimal_fraction *= 16
        integer_part = int(decimal_fraction)
        hexadecimal += hex_digits[integer_part]
        decimal_fraction -= integer_part
        if decimal_fraction == 0:
            break
    return hexadecimal

# Example usage:
decimal_fraction = 0.625 # decimal fraction must between 0 and 1
hexadecimal_fraction = decimal_fraction_to_hexadecimal(decimal_fraction)
print('0.' + hexadecimal_fraction)
