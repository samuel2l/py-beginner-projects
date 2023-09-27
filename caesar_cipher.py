from math import *
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# def decrypt(txt,shft):
#     cipher=""
#     for i in txt:
#         old_index=alphabet.index(i)
#         new_index= (old_index - shft)%26
#         new_letter=alphabet[new_index]
#         cipher +=new_letter
#     print(cipher)
# def encrypt(txt,shft):
#     cipher= ""
#     for i in txt:
#         old_index= alphabet.index(i)
#         new_index= (old_index + shft) % 26
#         new_letter=alphabet[new_index]
#         cipher+=new_letter
#     print(cipher)
# direction = input("Type 'encrypt' to encrypt, type 'decrypt' to decrypt: ").lower()
# text = str(input("Type your message: ")).lower()
# shift = int(input("Type the shift number: "))
# if direction== 'encrypt':
#     encrypt(text,shift)
# elif direction=='decrypt':
#     decrypt(text,shift)
# besides using mod you can simply double the size of the alphabet array. linear search in index func is advantageous here
# here, since array size if now 52 you cant ever be out of range and lin search will stop once it finds the first alphabet
# and will not look for its duplicate you barb
# ENCRYPT AND DECRYPT IN ONE FUNCTION:
def caesar(txt,shft,direction):
    cipher = ""

    for i in txt:
        if i.isalpha():
            old_index = alphabet.index(i)
            if direction == "encrypt":
                new_index = (old_index + shft) % 26
            elif direction == "decrypt":
                new_index = (old_index - shft) % 26

            new_letter = alphabet[new_index]

            cipher += new_letter
        else:
            cipher+=i
    print(cipher)
print(logo)
direction=input('enter whether decrypt or encrypt ')
word = input('Enter the word to en/decrypt ')
shiftt = int(input("enter the caesar key/shift "))

caesar(word , shiftt , direction)
