#Fungsi Filter List

def fillist(x):
    for idx, word in enumerate(x):
        lowword = word.lower()
        x[idx] = lowword
    search = input('Masukkan kata kunci: ').lower()
    b = (list(filter(lambda a: search in a, x)))
    for idx, word in enumerate(b):
        capword = word.capitalize()
        b[idx] = capword
    return print(b)    


# fillist(list_kata)

# #Fungsi duplikat map

def maplist(function,list_container):
    hasil =[]
    for item in list_container:
        hasil.append(function(item))
    return hasil
list_kata=['Merdeka', 'Hello', 'Hellos', 'Sohib', 'Kari Ayam']

# print(maplist(lambda x: x.lower(), list_kata))


# #Fungsi duplikat filter:

def filterlist(function,list_container):
    hasil = []
    for i in list_container:
        if function(i):
            hasil.append(i)
    return hasil

# print(filterlist(lambda x: 'K' in x, list_kata))



#Fungsi Jumlah Kata
def jumlah_kata(string):
    kata = {}
    for word in string.lower().split():
        if word in kata.keys():
            kata[word] += 1
        else:
            kata[word] = 1
    for keys, val in kata.items():
        print("Jumlah kata '{}' ada sebanyak {}".format(keys.capitalize(), val))        

kata = 'Aku baru makan nasi terus aku mau makan mie nanti malam'        

jumlah_kata(kata)
