# example
import sicpy

from sicpy.ciphers.caesar   import Caesar
from sicpy.ciphers.vigenere import Vigenere
from sicpy.ALPHAS.LATIN     import FRENCH

crypter = sicpy.Cryptobox()

alphabet = FRENCH
alphabet = sicpy.Alphabet('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

#plain_text = 'Jupiter knows more of all that weird\' stuff'
#plain_text = 'QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD'

# Class style
#############

#crypter = Caesar()
crypter = Caesar(alphabet)
plain_text = 'QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD'
key = -3
string = crypter.decipher(alphabet, key, plain_text)
print("original: \t", plain_text)
print("deciphered: \t", string)
print("Now Bruteforce: ")
string = crypter.bruteforce(25, alphabet, plain_text)
print(string)

print()

# Class with Object attributes
##############################

crypter.plain_text = 'CRYPTO IS SHORT FOR CRYPTOGRAPHY'
crypter.key = key
crypter.alphabet = alphabet
string = crypter.cipher()
print("original: \t", crypter.plain_text)
print("ciphered: \t", string)

# Class with partial attributes
###############################

string = crypter.cipher(key=crypter.key, alphabet=alphabet)
print("original: \t", crypter.plain_text)
print("ciphered: \t", string)


# Vigenere
plain_text = 'CRYPTO IS SHORT FOR CRYPTOGRAPHY'
key = 'ABCD'
crypter = Vigenere()
cipher_text = crypter.cipher(alphabet, key, plain_text)
string = crypter.decipher(alphabet, key, cipher_text)
print("original:\t", plain_text)
print("cipher: \t", cipher_text)
print("decipher:\t", string)

# Just enough to try 'AZYX' which has a de-key of ABCD
string = crypter.bruteforce(19010, alphabet, cipher_text)
for elem in string:
    print("key: ", elem[0], "\tde-key: ", elem[1], "\ttext: ", elem[2])

