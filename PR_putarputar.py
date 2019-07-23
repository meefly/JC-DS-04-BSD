import random

# Generate_x*y_angka
def number_generate(x):
    number = []
    pilihan = int(input('Pilih\n1.Angka urut\n2.Angka random\nMasukkan pilihan: '))
    if pilihan == 1:
        for i in range(x):
            temp_number =[]
            for j in range(x):
                temp_number.append((j+1)+(i*x))
            number.append(temp_number)
    elif pilihan == 2:            
        for i in range(x):
            temp_number = []
            for j in range(x):
                temp_number.append(random.randint(1,101))
            number.append(temp_number)   
    return number

# Print_angka
def print_angka(angka):
    for i in angka:
        z = ''
        for j in (range(len(angka))):
            z += str(i[j])
            z += ' '
        print(z)

#Memutar
def putarputar():
    ukuran = int(input('Masukkan ukuran: '))
    angka = number_generate(ukuran)
    print_angka(angka)
    putar = input('Putar ke arah?: ')
    kali = int(input('Putar berapa kali: '))
    if putar == 'Kanan' or putar == 'kanan':
        for c in range(kali):
            list_kanan = []
            for i in range(len(angka)):
                list_temp =[]
                for j in range((len(angka)-1),-1,-1):
                    list_temp.append(angka[j][i])
                list_kanan.append(list_temp)
            angka = list_kanan            
    elif putar == 'Kiri' or putar == 'kiri':
        for c in range(kali):
            list_kiri = []
            for i in range((len(angka)-1),-1,-1):
                list_temp =[]
                for j in range((len(angka))):
                    list_temp.append(angka[j][i])
                list_kiri.append(list_temp)    
            angka = list_kiri
    print_angka(angka)
                
while(True):
    angka = []
    putarputar()
    exit = input('Coba lagi [y/n]: ')
    if exit == 'y':
        True
    elif exit == 'n':
        print('Terima kasih')
        break    
