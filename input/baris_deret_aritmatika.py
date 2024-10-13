print("Program Barisan Deret Aritmatika")
print("================================")
print()

a = int(input("Masukkan Suku Awal : "))
n = int(input("Masukkan Banyak Suku : "))
b = int(input("Masukkan Beda : "))
print()

print("Barisan Aritmatika:")
for i in range(n):
    print(a + (i * b), end=" ")

deret_aritmatika = (2 * a + (n - 1) * b) * n // 2
print("\nDeret Aritmatika:", deret_aritmatika)