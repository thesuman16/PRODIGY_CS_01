letters = 'abcdefghijklmnopqrstuvwxyz'
#key = 3
#g ->j, j->g,(if key = 3) ||x->c, c->x (if key = 5)
#for encryption
num_letters = len(letters)

######### this is the long way of doing and wrire duplicate code for encryption and decryption ####
# def encrypt(plaintext, key):
#     ciphertext = ''
#     for letter in plaintext:
#         letter = letter.lower()
#         if not letter == ' ':
#             index = letters.find(letter)
#             if index == -1:
#                 ciphertext += letter
#             else:
#                 new_index = index + key
#                 if new_index >= num_letters:
#                     new_index -= num_letters
#                 ciphertext += letters[new_index]
#     return ciphertext
# # for decryption
# def decrypt(ciphertext, key):
#     plaintext = ''
#     for letter in plaintext:
#         letter = letter.lower()
#         if not letter == ' ':
#             index = letters.find(letter)
#             if index == -1:
#                 plaintext += letter
#             else:
#                 new_index = index + key
#                 if new_index < 0:
#                     new_index += num_letters
#                 plaintext += letters[new_index]
#     return plaintext
################## this is the short way of doing and write only one function for both encryption and decryption ####
def encrypt_decrypt(text, mode, key):
    result = ''
    if mode =='d':
       key = -key
        
    for letter in text:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                result += letter
            else:
                new_index = index + key
                if new_index >= num_letters:
                    new_index -= num_letters
                elif new_index < 0:
                    new_index += num_letters
                result += letters[new_index]
    return result
print()
print('Welcome to the Caesar Cipher Program')
print()
print('Do you want to encrypt or decrypt?')
user_input = input('Type e for encrypt or d for decrypt: ').lower() #to make the input case insensitive
print()
if user_input == 'e':
    print('You have chosen to encrypt')
    print()
    key = (int(input('Enter the key (1-26): ')))
    text = input('Enter the text to encrypt: ')
    ciphertext = encrypt_decrypt (text, key)
    print(f'The encrypted text is: {ciphertext}')
    
elif user_input == 'd':
    print('You have chosen to decrypt')
    print()
    key = int(input('Enter the key (1-26): '))
    text = input('Enter the text to decrypt: ')
    plaintext = encrypt_decrypt(text, key)  
    print(f'The decrypted text is: {plaintext}')

