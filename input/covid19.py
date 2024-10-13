print('Program menghitung Data Kasus COVID-19')

ptv = int(input('Kasus Terkonfirmasi Positif : '))
death = int(input('Kasus Kematian : '))
recov = int(input('Kasus Kesembuhan : '))

out=death+recov
act=ptv-out

print('==== Data Kasus COVID-19 ====')
print('Kasus Positif    : '+ str(ptv))
print('Kasus Kematian    : '+ str(death))
print('Kasus Pulih    : '+ str(recov))
print('Kasus Aktif    : '+ str(act))
print('Kasus Pasif    : '+ str(out))
print('=============================')