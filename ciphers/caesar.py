from main      import Cryptobox
from iterators import integer_iterator

def caesar_load():
    """ """
    Cryptobox.cipher       = caesar_cipher
    Cryptobox.key_inverse  = caesar_key_inverse
    Cryptobox.key_iterate = caesar_key_iterate
    Cryptobox.key_init     = caesar_key_init

def caesar_cipher(self, alpha, input_text, key):
    """ """
    output_text = ''
    for index, letter in enumerate(input_text):
        pos_mayus = alpha.mayus.find(letter)
        pos_minus = alpha.minus.find(letter)
        if pos_mayus != -1:
            output_text += \
              alpha.mayus[(pos_mayus + key) % alpha.length]
        elif pos_minus != -1:
            output_text += \
              alpha.mayus[(pos_minus + key) % alpha.length]
        else:
            output_text += input_text[index]
    return output_text

def caesar_key_inverse(self, alpha, key):
    """ """
    return alpha.length - key

def caesar_key_iterate(self, alpha, key):
    """
    need to pass alpha for consistency"""
    #return key + 1
    return integer_iterator(self, key)

caesar_key_init = 0
