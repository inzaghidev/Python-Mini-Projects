def pangkatRekursif(angka,pangkat):
   if pangkat == 0:
      return 1
   else:
      return angka * pangkatRekursif(angka,pangkat-1)

print('--------------------------------')
print('Program Pangkat Bilangan')
print('--------------------------------')

angka = int(input("Angka : "))
pangkat = int(input("Pangkat : "))

print('Hasil : ', pangkatRekursif(angka,pangkat))