import random

def decimal_to_hexadecimal(decimal):
    digits = "0123456789abcdef"
    integer_part = ""
    decimal_int = int(decimal)  # convert decimal to integer
    while decimal_int >= 16:
        digit = decimal_int % 16
        decimal_int = decimal_int // 16
        integer_part = digits[digit] + integer_part
    integer_part = digits[decimal_int] + integer_part
    
    fraction_part = ""
    for i in range(4): # amount digits
        decimal *= 16
        digit = int(decimal)
        fraction_part += digits[digit]
        decimal -= digit
    
    result = integer_part + "." + fraction_part
    return result


for i in range(10):
    random_decimal = random.random()
    random_hexadecimal = decimal_to_hexadecimal(random_decimal)
    print(random_hexadecimal)