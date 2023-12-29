# inputUser = input("Input Number: ")
# match inputUser:
#     case '1':
#         print('january')
#     case 2:
#         print('Feburary')
#     case 3:
#         print('march')
#     case 4:
#         print('April')
#     case 5:
#         print('May')
#     case 6:
#         print('June')
#     case 7:
#         print('July')
#     case 8:
#         print('August')
#     case 9:
#         print('September')
#     case 10:
#         print('Oct')
#     case 11:
#         print('November')
#     case 12:
#         print("December")
#     case _:
#         print('Invalid Input...')
# inputUser = input("Input Alphabet: ")
# match inputUser:
#     case 'a':
#         print('Vowel')
#     case 'e':
#         print('Vowel')
#     case 'i':
#         print('Vowel')
#     case 'o':
#         print('Vowel')
#     case 'u':
#         print('Vowel')
#     case _:
#         print("Consonant...")
        
inputUser = input("Input Alphabet: ")
if(inputUser == 'a' and inputUser == 'e' and inputUser == 'i' and inputUser == 'o' and inputUser == 'u'):
    print('Vowel')
else:
    print("Consonant")
    
