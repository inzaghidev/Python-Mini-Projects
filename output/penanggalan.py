import datetime

x = datetime.datetime.now()

thn = x.year
bln = x.month
bul = x.strftime("%B")
tgl = x.strftime("%d")
har = x.strftime("%w")
hari = x.strftime("%A")
harke = x.strftime("%j")
waktu = x.strftime("%X")
jam = x.strftime("%H")
mnt = x.strftime("%M")
dtk = x.strftime("%S")

if thn % 400 == 0:
    leap=366
elif thn % 100 == 0:
    leap=365
elif thn % 4 == 0:
    leap=366
else:
    leap=365

persen = 100/float(leap)*(float(harke)-1+(float(jam)/24)+(float(mnt)/1440)+(float(dtk)/86400))
harmun = 1+leap-int(harke)
permun = 100-persen

if hari == "Sunday":
    har = 7

print("Tahun                    : "+str(thn))
print("Bulan                    : "+str(bln)+" ("+str(bul)+")")
print("Tanggal                  : "+str(tgl))
print("Hari                     : "+str(har)+" ("+str(hari)+")")
print("Hari ke (dalam Setahun)  : "+str(harke))
print("Sisa Hari (Tahun depan)  : "+str(harmun))
print("Persentase dalam Setahun : "+str(round(persen, 6))+"%")
print("Persentase Hitung Mundur : "+str(round(permun, 6))+"%")
print("Jam                      : "+str(jam))
print("Menit                    : "+str(mnt))
print("Detik                    : "+str(dtk))

print()
print(str(hari)+", "+str(tgl)+" "+str(bul)+" "+str(thn))
print("Day-"+str(harke)+" ("+str(round(persen, 4))+"%)")
print(str(waktu))