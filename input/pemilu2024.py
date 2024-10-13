jumlah_vote = [0, 0, 0]

while True:
  print("Aplikasi Pemilihan Presiden Pemilu 2024")
  print("-----------------------------")
  print("01. Anies-Muhaimin = " + str(jumlah_vote[0]))
  print("02. Prabowo-Gibran = " + str(jumlah_vote[1]))
  print("03. Ganjar-Mahfud = " + str(jumlah_vote[2]))
  print("-----------------------------")
  pilihan = int(input("Masukan Pasangan Presiden :"))
  jumlah_vote[pilihan - 1] = jumlah_vote[pilihan - 1] + 1