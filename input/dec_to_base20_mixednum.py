def decimal_to_vigesimal(decimal):
    digits = "0123456789abcdef"
    integer_part = ""
    fractional_part = ""
    
    # convert integer part to vigesimal
    integer = int(decimal)
    while integer >= 20:
        integer, remainder = divmod(integer, 20)
        integer_part = digits[remainder] + integer_part
    integer_part = digits[integer] + integer_part
    
    # convert fractional part to vigesimal
    fractional = decimal - int(decimal)
    for _ in range(10): # amount of digits
        fractional *= 20
        digit = int(fractional)
        fractional_part += digits[digit]
        fractional -= digit
    
    return integer_part + "." + fractional_part

# Example usage:
decimal_number = 1234.5678
vigesimal_number = decimal_to_vigesimal(decimal_number)
print(vigesimal_number)