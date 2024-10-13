import random

def hexadecimal_integer():
    digits = "0123456789abcdef"
    result = ""

    # generate random integer part
    integer = random.randint(0, 16**2)  # amount digits of integers
    result = ""
    while integer >= 16:
        digit = integer % 16
        integer = integer // 16
        result = digits[digit] + result
    result = digits[integer] + result

    return result

for i in range(10):
    print(hexadecimal_integer())
