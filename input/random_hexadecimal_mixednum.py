import random

def random_hexadecimal():
    digits = "0123456789abcdef"
    
    # generate random integer part
    integer_part = random.randint(0, 16**2)  # amount digits of integers
    hexadecimal_integer = ""
    while integer_part >= 16:
        digit = integer_part % 16
        integer_part = integer_part // 16
        hexadecimal_integer = digits[digit] + hexadecimal_integer
    hexadecimal_integer = digits[integer_part] + hexadecimal_integer
    
    # generate random fraction part
    fraction_part = random.uniform(0, 1)
    hexadecimal_fraction = ""
    for i in range(4): # amount digits of fractions
        fraction_part *= 16
        digit = int(fraction_part)
        hexadecimal_fraction += digits[digit]
        fraction_part -= digit
    
    # combine integer and fraction parts
    result = hexadecimal_integer + "." + hexadecimal_fraction
    return result

# generate 10 random hexadecimal numbers
for i in range(10):
    random_hexadecimal_num = random_hexadecimal()
    print(random_hexadecimal_num)
