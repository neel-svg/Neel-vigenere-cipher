from itertools import product
from string import ascii_lowercase
from Vigenere_Cipher import decrypt_message, encrypt_message
from re import search


# generating keys for brute forcing, generated
def generate_keys(): #try do this in a for each loop so you can choose how many times to repeat according to most likely string lengths
    keywords = []
    keywords += [''.join(i) for i in product(ascii_lowercase, repeat=1)] #generating all one digit keys
    keywords += [''.join(i) for i in product(ascii_lowercase, repeat=2)] #generating all two digit keys
    keywords += [''.join(i) for i in product(ascii_lowercase, repeat=3)] #generating all three digit keys
    keywords += [''.join(i) for i in product(ascii_lowercase, repeat=4)] #generating all four digit keys
    return keywords #returning array of all keywords

# attempting to decipher the encrypted string
def decipher(encrypted): #decrypt each string using the key and check for words in wordlist.
    possible_txt = []
    possible_keys = generate_keys()
    for key in possible_keys: #iterating through possible keys
        possible_txt += decrypt_message(encrypted, key) #decrypting message into a list
        wordlist = open('wordlist.txt') #opening wordlist
        wordlist.readlines()
        wordlist.close()

        if search(wordlist, possible_txt): #attempted to compare wordlist to each of the decrypted messages and prompt user if match is found.

        return possible_txt


# run the decryption function against all possible key values
# check against dictionary for substrings, which has most amount of substrings existing in it is the answer


if __name__ == '__main__':
    print(generate_keys())