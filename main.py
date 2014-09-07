#from alphabet import Alphabet

class Cryptobox:
    """
        Note that only the alphabet is case sensitive, not the ciphers,
        that means that if a lowercase is found in the plain text, the cipher-text
        will be made by ciphering the upper case leter.

        And beware that plain_text & cipher_text will never be overited by
        self.cipher, self.decipher or self.bruteforce,
        if you wish to do so, you can do it yourself as follows:
        >>> instance_of_Cryptobox.cipher_text =
             instance_of_Cryptobox.cypher(plain_text)
    """
    #def __init__(self):
        #self.alphabet    = Alphabet()
        #self.plain_text  = ""
        #self.cipher_text = ""

        # SAIN DEFAULTS COULD BE:
        #self.alphabet = Alphabets.latin
        #self.plain_text = ""
        #self.cipher_text = ""
        #nothing for key, different types are possible

    #def cipher(self):
        #""" """
        #pass

    def decipher(self, alphabet=None, input_text=None, key=None):
        """ """

        if alphabet == None:
            alphabet = self.alphabet
        if input_text == None:
            input_text = self.cipher_text # NEED TO DECIDE IF THIS IS OK
        if key == None:
            key = self.key

        return self.cipher(alphabet, input_text,
                           self.key_inverse(alphabet, key))

    def bruteforce(self, times, alphabet=None, input_text=None):
        """ """

        if alphabet == None:
            alphabet = self.alphabet
        if input_text == None:
            input_text = self.cipher_text # NEED TO DECIDE IF THIS IS OK

        key = self.key_init
        brutebox = []
        for i in range(0, times):
            brutebox.append([key, self.key_inverse(alphabet, key),
                             self.decipher(alphabet, input_text, key)])
                             #self.cipher(alphabet, input_text, key)])
            key = self.key_iterate(alphabet, key)
        return brutebox

