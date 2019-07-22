#Fungsi Main Menu

def menu():
    print('Main menu \n 1. Lihat full dictionary \n 2. Isi Dictionary \n 3. Searching dictionary \n 4. Keluar' )
    pilihan = int(input('Masukkan pilihan: '))
    return pilihan

#Fungsi Mengisi Dictionary

def isidict(x):
        kali = int(input('Berapa kali masukkan dictionary?: '))
        for i in range(kali):
            a = int(input('1. String \n2. Number \n Masukkan pilihan: '))
            if a > 2 or  a < 0:
                print('Invalid input, try again')
                break
            elif a == 1 :
                b = input('Masukkan key: ')
                c = input('Masukkan value: ')
                x[b] = c
            else:
                b = input('Masukkan key: ')     
                c = int(input('Masukkan value: '))    
                x[b] = c
        return x    

#Fungsi Kotak di Awal
def awal():
        z =''
        for i in range (34):
                z += '_'
        z+='\n|      Key       |     Value      |\n|'
        for j in range(32):
                z+= '_'
                if j == 15:
                        z+= '|'
        z+='|'               
        return print(z)

#Fungsi Menu Utama
def utama():
        x ={}
        while(True):
                choice = menu()
                if choice == 4:
                        print('Thank you')
                        break
                if choice == 1:
                        print('Full Dictionary: \n')
                        awal()
                        key = list(x.keys())
                        val = list(x.values())
                        for i in range(len(x)):
                                if type(val[i]) == type('str'):
                                        print("|      '",key[i],"'  |    '",str(val[i]),"'   |")
                                elif type(val[i]) == type(1):
                                        print("|      '",key[i],"'  |   ",str(val[i]),"   |")         
                                z='|______'
                                for a in range(len(str(key[i]))):
                                        z+='_'
                                z+='______|______'
                                for b in range(len(str(val[i]))):
                                        z+= '_'
                                z+='______|'
                                print(z)                
                if choice == 2:   
                        x = isidict(x)
                if choice == 3:
                        search = str(input('Keyword: ')).lower()
                        filtered_key = (list(filter(lambda key: search in key.lower(), x)))
                        value = []
                        for key in filtered_key:
                                value.append(x[key])
                        print('Search result: \n')
                        awal()
                        for i in range(len(filtered_key)):
                                if type(value[i]) == type('str'):
                                        print("|    '{}'      |      '{}'   |".format(filtered_key[i], value[i]))
                                elif type(value[i]) == type(1):
                                        print("|    '{}'     |      {}    |".format(filtered_key[i], value[i])) 
                                z='|_________________|_______________|'
                                print(z)       

utama()

