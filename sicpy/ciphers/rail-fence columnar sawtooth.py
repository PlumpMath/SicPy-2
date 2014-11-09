from sicpy.cryptobox import Cryptobox
from sicpy.utils.iterators import integer_iterator

class Col_rail_sawtooth(Cryptobox):
    """ """
    def __init__(self, alphabet=None, key=None, plain_text=None,
                 cipher_text=None):
        """ """
        Cryptobox.__init__(self, alphabet, key, plain_text, cipher_text)
        self.key_init = 0       # Not necessary for know,
        # will be if __init__ is defined for Cryptobox,
        # later on
        pass
        self.key_init = 0


    def cipher(self, alphabet=None, input_text=None, key=None):
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

        return output_text

    def decipher(self, alphabet=None, key=None, input_text=None):
        """ """
        return Cryptobox.decipher(self, alphabet, key, input_text)

    def bruteforce(self, times=None, alphabet=None, input_text=None):
        """ """
        # initialise times to alphabet length
        if times == None:
            if alphabet == None:
                times = self.alphabet.length
            else:
                times = alphabet.length

        return Cryptobox.bruteforce(self, times, alphabet, input_text)

    def key_inverse(self, alphabet=None, key=None):
        """ """

        # Variable inference
        if alphabet == None:
            alphabet = self.alphabet
        if key == None:
            key = self.key
        # Main code
        return alphabet.length - key

    def key_iterate(self, alphabet=None, key=None):
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

