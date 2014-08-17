from main      import Cryptobox
from iterators import alphabet_iterator

def vigenere_load():
    """ """
    Cryptobox.cipher       = vigenere_cipher
    Cryptobox.key_inverse  = vigenere_key_inverse
    Cryptobox.key_iterate = vigenere_key_iterate
    Cryptobox.key_init     = vigenere_key_init

def vigenere_cipher(self, alpha, input_text, key):
    """ """
    output_text = ''
    key_length  = len(key)
    counter     = 0
    for index, letter in enumerate(input_text):
        pos_mayus = alpha.mayus.find(letter)
        pos_minus = alpha.minus.find(letter)
        if pos_mayus != -1 :
            caesar_key = alpha.mayus.find(key[counter % key_length])
            output_text += \
              alpha.mayus[(pos_mayus + caesar_key) % alpha.length]
            counter += 1
            counter = counter % key_length
        elif pos_minus != -1:
            caesar_key = alpha.mayus.find(key[counter % key_length])
            output_text += \
              alpha.mayus[(pos_minus + caesar_key) % alpha.length]
            counter += 1
            counter = counter % key_length
        else:
            output_text += input_text[index]
    return output_text

def vigenere_key_inverse(self, alpha, key):
    """ """
    inverse_key = ''
    for letter in key:
        index = (alpha.length - alpha.mayus.find(letter)) % alpha.length
        inverse_key += alpha.mayus[index]
    return inverse_key

def vigenere_key_iterate(self, alpha, key):
    """ """
    return alphabet_iterator(self, alpha, key)

vigenere_key_init = 'A'
