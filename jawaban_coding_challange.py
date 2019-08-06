#Create a function That return the highest x-sequence from the given number (2-5)

# def get_highest_xnum(num, sequence):
#    from math import floor,pow

#    if num < pow(10,sequence) or sequence >5:
#       print('Input valid num or sequence')
#    else:
#       angka = []
#       while (num > 0):
#          angka.append(num%10)   
#          num = floor(num/10)
#       highest = 0
#       for idx in range(len(angka)-1,sequence-2,-1):
#          test = ''
#          for i in range(sequence):
#             test += str(angka[idx-i])   
#          if int(test) > highest:
#             highest = int(test)
#       print('The highest {}-number is {}'.format(sequence,highest))
      
# get_highest_xnum(87173114, 5)

#Create Sum List Triangle, with the highest part is highlighted

# def sum_triangular_numbers(n):
#    if n < 0:
#       return 0
#    else:    
#       number = []
#       for i in range(1,n+1):
#          number_temp = []
#          for j in range(i,i*2):
#             if i == 1 or i == 2:
#                number_temp.append(j)
#             else:
#                number_temp.append(j + number[i-3][-1])
#          number.append(number_temp)
#       sum_ = 0
#       number_print = number
#       z = ''
#       for item in number:
#          sum_ += item[-1]
#       for item in number_print:
#          item[-1] = [item[-1]]
#       for item in number_print:
#          for idx, val in enumerate(item):
#             z+=str(item[idx])
#             z+=' '
#          z+='\n'
#       print(z)        
#       return print('sum of each last part of the triangle is {}'.format(sum_))

# sum_triangular_numbers(8)