import math

x = float(input("Input number of power :"))
n = int(input("Input number of series :"))

e_to_x = 0
for i in range(n):
    e_to_x += x**i/math.factorial(i)
    
print(e_to_x)