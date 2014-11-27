from sicpy.alphabet     import Alphabet
from sicpy.ALPHAS.LATIN import LATIN

class Cryptobox:
    """
        Note that only the alphabet is case sensitive, not the ciphers,
        that means that if a lowercase is found in the plain text,
        the cipher-text will be made by ciphering the upper case letter.

        And beware that plain_text & cipher_text will never be overiten by
        self.cipher, self.decipher or self.bruteforce,
        if you wish to do so, you can do it yourself as follows:
        >>> instance_of_Cryptobox.cipher_text =
             instance_of_Cryptobox.cypher(plain_text)
    """

    def __init__(self, alphabet=None, key=None, plain_text=None,
                 cipher_text=None):
        """
            .... def, bla bla

            Some default names are implemented,
            those are only compulsory if you wish to omit them in method calls.
            This is why a default name needs to be chosen for all the ciphers,
            and is implemented here as a reference for all ciphers.
        """
        if alphabet == None:
            self.alphabet = LATIN
        else:
            self.alphabet = alphabet

        if key == None:
            self.key = None # can be numeric of alphabetic (a string)
        else:
            self.key = key

        if plain_text == None:
            self.plain_text  = ""
        else:
            self.plain_text = plain_text

        if cipher_text == None:
            self.cipher_text = ""
        else:
            self.cipher_text = cipher_text

        self.key_init = None

    #def cipher(self):
        #""" """
        #pass

    def decipher(self, alphabet=None, key=None, input_text=None):
        """ """

        if alphabet == None:
            alphabet = self.alphabet
        if input_text == None:
            input_text = self.cipher_text
        if key == None:
            key = self.key

        return self.cipher(alphabet, self.key_inverse(alphabet, key),
                           input_text)

    def bruteforce(self, times, alphabet=None, input_text=None):
        """ """

        if alphabet == None:
            alphabet = self.alphabet
        if input_text == None:
            input_text = self.cipher_text

        key = self.key_init
        brutebox = []
        for i in range(0, times):
            brutebox.append([key, self.key_inverse(alphabet, key),
                             self.decipher(alphabet, key, input_text)])
                             #self.cipher(alphabet, key, input_text)])
            key = self.key_iterate(alphabet, key)
        return brutebox

    def strip_non_alphabetic(self, alphabet=None, input_text=None):

        if alphabet == None:
            alphabet = self.alphabet
        if input_text == None:
            input_text = self.plain_text

        stripped = ''
        for letter in input_text:
            if letter in alphabet.alpha:
                stripped += letter

        return stripped
