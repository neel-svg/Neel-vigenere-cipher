# # Author: Neel Paranjape
# # Date: 24/04/2021
# # Description:
# # A class consisting of functions to encode and decode sample text with a given key using the Vigenere cipher.

alphabet = 'abcdefghijklmnopqrstuvwxyz'

alphabet_count = len(alphabet)


def encrypt_char(plaintext, key):
    key_index = alphabet.index(key)
    plaintext_index = alphabet.index(plaintext)

    cipher_char = alphabet[(plaintext_index + key_index) % alphabet_count]

    return cipher_char


def decrypt_char(ciphertext, key):
    key_index = alphabet.index(key)
    ciphertext_index = alphabet.index(ciphertext)

    decipher_char = alphabet[(ciphertext_index - key_index) % alphabet_count]

    return decipher_char


def encrypt_message(message, key):
    encrypted_message = ''

    for (message_index, message_character) in enumerate(message):
        key_index = message_index % len(key)
        key_char = key[key_index]
        encrypted_message += encrypt_char(message_character, key_char)
    return encrypted_message


def decrypt_message(encrypted_message, key):
    decrypted_message = ''
    for (message_index, message_character) in enumerate(encrypted_message):
        key_index = message_index % len(key)
        key_char = key[key_index]
        decrypted_message += decrypt_char(message_character, key_char)
    return decrypted_message


# if __name__ == '__main__':
#     plaintext = "secretmessage"
#     keytext = "key"
#     cipher_text = encrypt_message(plaintext, keytext)
#     decipher_text = decrypt_message(cipher_text, keytext)
#
#     print("Message: " + plaintext)
#     print("Password: " + keytext)
#     print("The ecnrypted message is: " + cipher_text)
#     print("The decrypted message is: " + decipher_text)
