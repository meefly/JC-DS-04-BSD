
# No1

x=4
y=3
z=2
w = ((x+y*z)/(x*y))**z
print(w)

#No2

angka = int(input("Silahkan masukkan angka berapapun: "))
print("Kuadrat dari "+ str(angka) + " = " + str(angka**2))

# # No3 (total hari dijadikan satu - satu ke tahun, bulan, etc.)

import math
total_hari1 = int(input("masukkan hari: "))
tahun1 = str(math.floor(total_hari1/360))
bulan1 = str(math.floor((total_hari1 % 360)/30))
minggu1 = str(math.floor(((total_hari1 % 360)%30)/7))
hari1 = str(math.floor(((total_hari1 % 360)%30)%7))
print(tahun1 + " tahun " + bulan1 + " bulan " +  minggu1 + " minggu " + hari1 + " hari ")

#No4

# Andi(A) + Budi(B) = 49
# A/B = 4/10
# 10A = 4B
# B = 10A / 4
# A = 49 - B
# B = 490 -10B/4
# 4B = 490 - 10B
# B = 490/14

umur_budi = 490/14
umur_andi = 49 - umur_budi
print(umur_andi + 2)
print(umur_budi + 2)


# No5
word = input('Kata: ')
cari = input('Karakter yang ingin dicari: ')
print(word.split(cari))
print(int(len(word.split(cari)))-1)


# No6
jam_berangkat = int(input('Jam Berangkat: '))
menit_berangkat = int(input('Menit Berangkat: '))

jarak = int(input("Jarak antara kendaraan?: "))
kecepatan_a = int(input("Kecepatan kendaraan a?: "))
kecepatan_b = int(input("Kecepatan kendaraan b?: "))

tabrakan_menit = (
    jarak/(kecepatan_a + kecepatan_b))*60
print(str(tabrakan_menit) + ' menit')

jam = tabrakan_menit//60
menit = tabrakan_menit%60

print('jam ' + str(int(jam_berangkat + jam)) + ' lewat ' + str(int(menit_berangkat + menit)) +' menit')

#jam 10.12 WIB
