from main      import Cryptobox
from iterators import integer_iterator

from types import MethodType

def caesar_load(crypto_instance):
    """ """
    crypto_instance.cipher      = MethodType(caesar_cipher, crypto_instance)
    crypto_instance.key_inverse = MethodType(caesar_key_inverse, crypto_instance)
    crypto_instance.key_iterate = MethodType(caesar_key_iterate, crypto_instance)
    crypto_instance.key_init    = caesar_key_init
    #return crypto_instance

class Caesar(Cryptobox):
    """ """
    def __init__(self):
        """ """
        # Not necessary for know,
        # will be if __init__ is defined for Cryptobox,
        # later on
        pass

        caesar_load(self)

def caesar_cipher(self, alphabet=None, input_text=None, key=None):
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
    for index, letter in enumerate(input_text):
        pos = alphabet.alpha.find(letter)
        if pos != -1:
            output_text += alphabet.alpha[(pos + key) % alphabet.length]
        else:
            output_text += input_text[index]
    return output_text

def caesar_key_inverse(self, alphabet=None, key=None):
    """ """

    # Variable inference
    if alphabet == None:
        alphabet = self.alphabet
    if key == None:
        key = self.key
    # Main code
    return alphabet.length - key

def caesar_key_iterate(self, alphabet=None, key=None):
    """
    need to pass alphabet for consistency"""

    # Variable inference
    #if alphabet == None:
    #    alphabet = self.alphabet
    if key == None:
        key = self.key
    # Main code
    return integer_iterator(self, key)
    #return key + 1

caesar_key_init = 0
