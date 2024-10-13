array = []
total = 0
n = int(input("Banyaknya Data : "))
for x in range(n):
    nilai = float(input("Data ke-{} : ".format(x+1)))
    array.append(nilai)
print("\nNilai Total     : {}".format(sum(array)))
print("Nilai Rata-rata : {}".format(sum(array)/n))