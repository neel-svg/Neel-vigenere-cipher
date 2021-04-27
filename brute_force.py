from itertools import product
from string import ascii_lowercase
from Vigenere_Cipher import decrypt_message, encrypt_message
from re import search
import enchant


def generate_keys():
    keywords = []
    keywords += [''.join(i) for i in product(ascii_lowercase, repeat=1)]
    keywords += [''.join(i) for i in product(ascii_lowercase, repeat=2)]
    keywords += [''.join(i) for i in product(ascii_lowercase, repeat=3)]
    keywords += [''.join(i) for i in product(ascii_lowercase, repeat=4)]
    return keywords


def decipher(encrypted):
    possible_txt = []
    possible_keys = generate_keys()
    for key in possible_keys:
        possible_txt += decrypt_message(encrypted, key)
        wordlist = open('wordlist.txt')
        wordlist.readlines()
        wordlist.close()

        if search(dictionary, possible_txt):

    # checking for substrings in possible text, if a substring from the dictionary occurs, stop program and promt user, else continue
        return possible_txt


# run the decryption function against all possible key values
# check against dictionary for substrings, which has most amount of substrings existing in it is the answer


if __name__ == '__main__':
    plaintext = "secretmessage"
    keytext = 'ke'
    possible_key = generate_keys()
cipher_text = encrypt_message(plaintext, keytext)
decipher_text = decipher(cipher_text)

print("Message: " + plaintext)
print("Password: " + keytext)
print("The encrypted message is: " + cipher_text)
print("The decrypted message is: " + decipher_text)


