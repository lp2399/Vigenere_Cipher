import re

def text_to_numerical_val_list(input_text):
    regex = re.compile('[^a-zA-Z]')
    input_text = regex.sub('', input_text)
    input_text = re.sub(r"\s+", "", input_text, flags=re.UNICODE)
    input_text = input_text.lower()
    text_char_to_numerical_value_list = []
    for character in input_text:
        numerical_value = ord(character) - 97
        text_char_to_numerical_value_list.append(numerical_value)
    return text_char_to_numerical_value_list    

def encipher(plaintext,key): 
    plaintext_numerical_val_list= text_to_numerical_val_list(plaintext)
    key_length = len(key)
    key_numerical_val_list = text_to_numerical_val_list(key)
    cipher_values = []
    j = 0
    for i in plaintext_numerical_val_list:
        if(j==key_length):
            j = 0
        cipher_val = i+key_numerical_val_list[j]  
        cipher_values.append(chr(((cipher_val)% 26)+97))
        j = j+1
    cipher_text = ''.join(str(char) for char in cipher_values)
    return "Cipher text:  "+cipher_text.upper()
  
def decipher(ciphertext,key):
    cipher_text_to_numerical_val_list = text_to_numerical_val_list(ciphertext)
    key_length = len(key)
    cipher_key_to_numerical_val_list = text_to_numerical_val_list(key)
    deciphered_values = []
    j = 0
    for i in cipher_text_to_numerical_val_list:
        if(j==key_length):
            j = 0
        deciphered_val = i-cipher_key_to_numerical_val_list[j]  
        deciphered_values.append(chr(((deciphered_val)% 26)+97))
        j = j+1
    deciphered_text = ''.join(str(char) for char in deciphered_values)
    return "Deciphered text:  "+deciphered_text.lower()

print(encipher("Vigenere's cipher method is not secure and should only be used for fun","Key")) # takes in a paramter of strings both plaintext and key
#Terminal output : Cipher text: FMEORCBIQMMNRIPWIRRSBSWLYXQOGSBIYXHQRSSVHMXPWLISCIBPSPPYL
print(decipher("FMEORCBIQMMNRIPWIRRSBSWLYXQOGSBIYXHQRSSVHMXPWLISCIBPSPPYL","Key")) # takes in a paramter of strings both ciphertext and key, requires the key
#Terminal output : Deciphered text:  vigeneresciphermethodisnotsecureandshouldonlybeusedforfun
