from main      import Cryptobox
from iterators import alphabet_iterator

from types import MethodType

def vigenere_load(crypto_instance):
    """ """
    crypto_instance.cipher      = \
            MethodType(vigenere_cipher, crypto_instance)
    crypto_instance.key_inverse = \
            MethodType(vigenere_key_inverse, crypto_instance)
    crypto_instance.key_iterate = \
            MethodType(vigenere_key_iterate, crypto_instance)
    crypto_instance.key_init    = vigenere_key_init
    #return crypto_instance

class Vigenere(Cryptobox):
    """ """
    def __init__(self):
        """ """
        # Not necessary for know,
        # will be if __init__ is defined for Cryptobox,
        # later on
        pass

        vigenere_load(self)

def vigenere_cipher(self, alphabet=None, input_text=None, key=None):
    """ """

    # Variable inference
    if alphabet == None:
        alphabet = self.alphabet
    if input_text == None:
        input_text = self.plain_text
    if key == None:
        key = self.key
    # Main code
    output_text = ''
    key_length  = len(key)
    counter     = 0
    for index, letter in enumerate(input_text):
        pos = alphabet.alpha.find(letter)
        if pos != -1:
            caesar_key = alphabet.alpha.find(key[counter % key_length])
            output_text += \
              alphabet.alpha[(pos + caesar_key) % alphabet.length]
            counter += 1
            counter = counter % key_length
        else:
            output_text += input_text[index]
    return output_text

def vigenere_key_inverse(self, alphabet=None, key=None):
    """ """

    # Variable inference
    if alphabet == None:
        alphabet = self.alphabet
    if key == None:
        key = self.key
    # Main code
    inverse_key = ''
    for letter in key:
        index = (alphabet.length - alphabet.alpha.find(letter)) \
                % alphabet.length
        inverse_key += alphabet.alpha[index]
    return inverse_key

def vigenere_key_iterate(self, alphabet=None, key=None):
    """ """

    # Variable inference
    if alphabet == None:
        alphabet = self.alphabet
    if key == None:
        key = self.key
    # Main code
    return alphabet_iterator(self, alphabet, key)

vigenere_key_init = 'A'
