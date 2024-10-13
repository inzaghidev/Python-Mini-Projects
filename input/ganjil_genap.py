print("-----------------------------------")
print("Program Deret Bilangan Ganjil Genap")
print("-----------------------------------")
print("1. Ganjil                          ")
print("2. Genap                           ")
print("-----------------------------------")

pil = int(input("Masukan Pilihan : "))
batas = int(input("Masukan Batas   : "))

if pil == 1:
    for x in range (1,batas):
        if x % 2 == 1:
            print(x, end=" ")
elif pil == 2:
    for x in range (1,batas):
        if x % 2 == 0:
            print(x, end=" ")
else:
  print("Invalid")