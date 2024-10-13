import math

def tetrasi(angka,tetra):
   if tetra == 0:
      return 1
   elif tetra == -1:
     return 0
   elif 0 <= tetra <= 1:
     return angka ** tetra
   elif -1 <= tetra <= 0:
     return tetra+1
   else:
      return angka ** tetrasi(angka,tetra-1)

angka = float(input("Angka : "))
tetra = float(input("Tetrasi : "))

print('Hasil : ', tetrasi(angka,tetra))