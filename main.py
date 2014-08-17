#from alphabet import Alphabet

class Cryptobox:
    """
        Note that only the alphabet is case sensitive, not the ciphers,
        that means that if a lowercase is found in the plain text, the cipher-text
        will be made by ciphering the upper case leter
    """
    #def __init__(self):
        #self.alphabet    = Alphabet()
        #self.plain_text  = ""
        #self.cipher_text = ""

    #def cipher(self):
        #""" """
        #pass

    def decipher(self, alphabet, input_text, key):
        """ """
        return self.cipher(alphabet, input_text,
                           self.key_inverse(alphabet, key))

    def bruteforce(self, alphabet, input_text, times):
        """ """
        key = self.key_init
        brutebox = []
        for i in range(0, times):
            brutebox.append([key, self.key_inverse(alphabet, key),
                             self.decipher(alphabet, input_text, key)])
                             #self.cipher(alphabet, input_text, key)])
            key = self.key_iterate(alphabet, key)
        return brutebox

