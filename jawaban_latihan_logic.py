
#Soal 1
angka1 = int(input('Masukkan angka: '))
angka2 = int(input('Masukkan angka: '))
if (angka1%2 == 0 ):
    print('Angka {}, dan bukan {} tergolong bilangan GENAP!'.format(angka1, angka2 ))
else:
    print('Angka {} tergolong bilangan GANJIL!'.format(angka))    


# #Soal 2
massa = float(input('Masukkan Massa(kg): '))
tinggi = float(input('Masukkan Tinggi(cm): '))
tinggi_m = tinggi/100


if imt < 18.5:
    k= 'BERAT BADAN KURANG!'
elif (imt >= 18.5 and imt <= 24.9):
    k= 'BERAT BADAN IDEAL!'
elif (imt >= 25.0 and imt <= 29.9):
    k= 'BB BERLEBIH!'
elif (imt >= 30.0 and imt <= 39.9):
    k= 'BB SANGAT BERLEBIH!'
else: 
    k= 'OBESITAS'

print ('Massa {} kg & tinggi {} m'.format(massa, tinggi_m))
print ('IMT = ' + str(imt) + ', '+ k)
