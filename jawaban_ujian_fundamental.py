#Soal Nomor 1

# def calculate_years(principal, interest, tax, desired):
#     year = 0
#     while(principal < desired):
#         principal = principal + ((principal*interest) - ((principal*interest)*tax))
#         year += 1
#     return year    
# print(calculate_years(1200, 0.17, 0.05, 2000))

#Soal Nomor 2
# def expanded_form(nomor): 
#     from math import floor,pow
#     angka = []
#     while(nomor > 0):
#         angka.append(nomor%10)
#         nomor = floor(nomor/10)
#     for idx,val in enumerate(angka):
#         angka[idx] = int(val * pow(10,idx))
    
#     z =''
#     for idx in range(len(angka)-1,-1,-1):
#         if angka[idx] != 0 and idx != 0:
#             z += str(angka[idx])
#             z += ' + '
#         elif angka[idx] !=0 and idx == 0:
#             z += str(angka[idx])                        
#     return z
# print(expanded_form(2))

#Soal Nomor 3

# def tower_builder(n_floors, block_size) :
#     w,h = block_size
#     arr = []
#     for i in range(1,n_floors*2,2) :
#         output = ''
#         output += ((n_floors * w) - (i + 1)) * ' '
#         output += (i * w) * '*'
        
#         for j in range(h) :
#             arr.append(output)
    
#     return arr

# print(tower_builder(6, (2,1)))
# for item in tower_builder(3, (2,3)) :
#     print(item)

