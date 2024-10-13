def ack(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m - 1, 1)
    elif m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))
    else:
        return ack(m, n)
 
print("Ackermann Function A(x, y)")
x = int(input("Insert value of x : "))
y = int(input("Insert value of y : "))

A = ack(x, y)

print("A("+str(x)+", "+str(y)+") = "+str(A))