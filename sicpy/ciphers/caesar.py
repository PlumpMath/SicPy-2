from sicpy.cryptobox       import Cryptobox
from sicpy.utils.iterators import integer_iterator

class Caesar(Cryptobox):
    """ """
    def __init__(self, alphabet=None, key=None, plain_text=None,
                 cipher_text=None):
        """ """
        Cryptobox.__init__(self, alphabet, key, plain_text, cipher_text)
        self.key_init = 0

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
        for index, letter in enumerate(input_text):
            pos = alphabet.alpha.find(letter)
            if pos != -1:
                output_text += alphabet.alpha[(pos + key) % alphabet.length]
            else:
                output_text += input_text[index]
        return output_text

    def decipher(self, alphabet=None, key=None, input_text=None):
        """ """
        return Cryptobox.decipher(self, alphabet, key, input_text)

    def bruteforce(self, times=None, alphabet=None, input_text=None):
        """ """
        # initialise times to alphabet length if not specified
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
        passes alphabet for consistency
        """

        # Variable inference
        #if alphabet == None: # Not necessary as not used
        #    alphabet = self.alphabet
        if key == None:
            key = self.key
        # Main code
        return integer_iterator(self, alphabet, key)

    # # is this good?
    # # edit: what for?
    # def key_out_of_bounds(self, alphabet=None, key=None):
    #     # Variable inference
    #     if alphabet == None:
    #         alphabet = self.alphabet
    #     if key == None:
    #         key = self.key
    #     # Main code
    #     # should return true or false? or rather give back the correct key
    #     if key >= 1 or key < alphabet.length:
    #         #return False
    #         return key
    #     else:
    #         #return True
    #         return key % alphabet.length


