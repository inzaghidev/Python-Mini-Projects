def reVal(num):
    if (num >= 0 and num <= 9):
        return chr(num + ord('0'))
    else:
        return chr(num - 10 + ord('A'))
# Utility function to reverse a string
def strev(str):
    len = len(str)
    for i in range(int(len / 2)):
        temp = str[i]
        str[i] = str[len - i - 1]
        str[len - i - 1] = temp
# Function to convert a given decimal
# number to a base 'base' and
def fromDeci(res, base, inputNum):
    index = 0 # Initialize index of result
    # Convert input number is given base
    # by repeatedly dividing it by base
    # and taking remainder
    while (inputNum > 0):
        res+= reVal(inputNum % base)
        inputNum = int(inputNum / base)
    # Reverse the result
    res = res[::-1]
    return res
    
# Driver Code
print("Program mencetak Konversi dari Desimal")
print("Program prints Conversion from Decimal")
print("===========================================")
base = int(input("Input Base : "))
res = ""

for inputNum in range(0, base):
    print(inputNum,"[",base,"] = ",fromDeci(res, base, inputNum))

# https://www.geeksforgeeks.org/convert-base-decimal-vice-versa (Konversi Sistem Bilangan dari Desimal ke Basis apapun dan sebaliknya)