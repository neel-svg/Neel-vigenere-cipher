# # Author: Neel Paranjape
# # Date: 24/04/2021
# # Description:
# # A function to encode and decode sample text with a given key using the Vigenere cipher.

from Vigenere_Cipher import encrypt_char, encrypt_message, decrypt_char, decrypt_message


def key_length(encrypted):
    pass




def decipher(encrypted, possible_key):
    pass
    # determine n combinations for n length of key
    # try all combinations one by one
    # dynamically compare all outputs against english dictionary words, stop when english text is found
































if __name__ == '__main__':
    plaintext = "secretmessage"
    keytext = "key"
    cipher_text = encrypt_message(plaintext, keytext)
    decipher_text = decrypt_message(cipher_text, keytext)

    print("Message: " + plaintext)
    print("Password: " + keytext)
    print("The encrypted message is: " + cipher_text)
    print("The decrypted message is: " + decipher_text)
