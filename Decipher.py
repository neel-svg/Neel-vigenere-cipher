# # Author: Neel Paranjape
# # Date: 24/04/2021
# # Description:
# # A function to encode and decode sample text with a given key using the Vigenere cipher.
import collections
from collections import Counter
from Vigenere_Cipher import encrypt_char, encrypt_message, decrypt_char, decrypt_message

#identifying varying sequences within the encrypted string
def sequence_occurrences(encrypted):
    out = []
    for length in range(2, 7): #range for potential length of key
        out += sequence_spacing(encrypted, length)
    return out


#getting factors of the numbers
def get_factors(number):
    factors = []
    if number < 2: #factors less than 2 are futile
        return []
    else:
        for i in range(2, number + 1):
            if number % i == 0: #if factor
                factors.append(i)
    return factors


def common_factors(sequence_values):
    factors = []
    # loop over array of sequence values
    for i in sequence_values:
        factors += get_factors(i)
    return factors
    # return list of all factors
    # filter out and return most common factors


# find all factors with highest occurrence and sort accordingly
def highest_occurrence(factors):
    sorted_occurrences = []
    sorted_occurrences += Counter(factors).most_common() #sort occurrances in terms of most common factors
    highest = sorted_occurrences[0][1]
    sorted_occurrences = [i[0] for i in sorted_occurrences if i[1] == highest] #filtering out number of occurrences and defining number.

    return sorted_occurrences


# sequence spacing function determines individual sequences
def sequence_spacing(encrypted, sequence_length):
    sequence_spacings = []
    string_length = len(encrypted)
    for i in range(0, string_length - sequence_length + 1):
        sequence = encrypted[i:i + sequence_length]
        # how many times sequence appears, frequency analysis
        # distance between sequences
        for x in range(i + sequence_length, string_length - sequence_length):
            test_sequence = encrypted[x:x + sequence_length]
            if test_sequence == sequence:
                print(test_sequence)
                sequence_spacings.append(x - i)
    return sequence_spacings

#attemped to generate the subkeys, first stripped the encrypted string of all non letter characters.
def generate_subkeys(encrypted, subkey_length):
    encrypted = encrypted.sub("[^a-zA-Z0-9]+", "", encrypted)
    subkeys = []
    i = 0
    while i < len(encrypted):
        subkeys.append(encrypted(i))
    i += subkey_length
    return "".join(subkeys)





def key_length(encrypted):
    pass


def decipher(encrypted, possible_key):
    pass
    # determine n combinations for n length of key
    # try all combinations one by one
    # dynamically compare all outputs against english dictionary words, stop when english text is found



if __name__ == '__main__':
    plaintext = "hellomynameisbobandilikeapplesandpearsbutifyouseemeontvyouaremehellohello"
    keytext = "key"
    cipher_text = encrypt_message(plaintext, keytext)
    decipher_text = decrypt_message(cipher_text, keytext)

    print("Message: " + plaintext)
    print("Password: " + keytext)
    print("The encrypted message is: " + cipher_text)
    print("The decrypted message is: " + decipher_text)
    print(sequence_occurrences(cipher_text))
    print(get_factors(20))
    print(common_factors(sequence_occurrences(cipher_text)))
    print('The key length is most likely: ')
    print(highest_occurrence(common_factors(sequence_occurrences(cipher_text))))


