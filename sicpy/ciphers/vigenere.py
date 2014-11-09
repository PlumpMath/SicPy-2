from sicpy.cryptobox       import Cryptobox
from sicpy.utils.iterators import alphabet_iterator

class Vigenere(Cryptobox):
    """ """
    def __init__(self, alphabet=None, key=None, plain_text=None,
                 cipher_text=None):
        """ """
        Cryptobox.__init__(self, alphabet, key, plain_text, cipher_text)
        self.key_init = 'A'

    def cipher(self, alphabet=None, key=None, input_text=None):
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
        caesar_key  = ''
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

    def decipher(self, alphabet=None, key=None, input_text=None):
        """ """
        return Cryptobox.decipher(self, alphabet, key, input_text)

    def bruteforce(self, times, alphabet=None, input_text=None):
        """ """
        return Cryptobox.bruteforce(self, times, alphabet, input_text)

    def key_inverse(self, alphabet=None, key=None):
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

    def key_iterate(self, alphabet=None, key=None):
        """ """

        # Variable inference
        if alphabet == None:
            alphabet = self.alphabet
        if key == None:
            key = self.key
        # Main code
        return alphabet_iterator(self, alphabet, key)
