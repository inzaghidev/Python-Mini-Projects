import math

def main():
    print("Program Barisan & Deret Geometri")
    print("================================\n")

    # Input nilai awal, rasio, dan banyaknya suku
    a = float(input("Masukkan Suku Awal (a) : "))
    r = float(input("Masukkan Rasio (r) : "))
    n = int(input("Masukkan Banyak Suku (n) : "))
    print()

    # Menampilkan Barisan Geometri
    print("Barisan Geometri :")
    for i in range(n):
        Un = a * math.pow(r, i)  # Menghitung suku ke-i (U_n)
        print(Un, end=" ")

    # Menghitung Jumlah Deret Geometri
    if r != 1:
        Sn = a * (1 - math.pow(r, n)) / (1 - r)
    else:
        Sn = a * n

    print("\nDeret Geometri (Jumlah S_n) :", Sn)

if __name__ == "__main__":
    main()