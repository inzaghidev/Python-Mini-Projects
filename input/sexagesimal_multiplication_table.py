def to_base60(number, base):
    custom_digits = "0123456789abcdefghijklmnopqrstuvwxyzαβγδεζηθικλμξΠϟρσςτυφχψω"
    result = ""
    while number > 0:
        number, remainder = divmod(number, base)
        result = custom_digits[remainder] + result
    if not result:
        result = "0"
    return result

# Prompt the user to enter the base 60 (Sexagesimal)
base = 60

# Define the range of numbers to include in the table
start = 0
end = 60

# Create the table header
print("   ", end="")
for i in range(start, end+1):
    print(to_base60(i, int(base)), end="  ")
print()

# Create the table body
for i in range(start, end+1):
    print(to_base60(i, int(base)), end=" |")
    for j in range(start, end+1):
        result = i * j
        result_base60 = to_base60(result, int(base))
        print("{:2}".format(result_base60), end=" ")
    print()
