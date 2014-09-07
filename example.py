# example

from main             import Cryptobox
from alphabet         import Alphabet
from ciphers.caesar   import caesar_load
from ciphers.caesar   import Caesar
from ciphers.vigenere import vigenere_load
from ALPHAS.LATIN import FRENCH

crypter = Cryptobox()

alphabet = FRENCH
alphabet = Alphabet('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

#plain_text = 'Jupiter knows more of all that weird\' stuff'
plain_text = 'QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD'

# Monkey patching style
#######################

key = -3
#caesar_load()
#crypter = caesar_load(crypter)
caesar_load(crypter)
string = crypter.decipher(alphabet, plain_text, key)
print("original: \t", plain_text)
print("deciphered: \t", string)
print("Now Bruteforce: ")
string = crypter.bruteforce(25, alphabet, plain_text)
print(string)

print()

plain_text = 'CRYPTO IS SHORT FOR CRYPTOGRAPHY'
key = 'ABCD'
#vigenere_load()
#crypter = vigenere_load(crypter)
vigenere_load(crypter)
cipher_text = crypter.cipher(alphabet, plain_text, key)
string = crypter.decipher(alphabet, cipher_text, key)
print("original:\t", plain_text)
print("cipher: \t", cipher_text)
print("decipher:\t", string)

# Just enough to try 'AZYX' which has a de-key of ABCD
string = crypter.bruteforce(19010, alphabet, cipher_text)
for elem in string:
    print("key: ", elem[0], "\tde-key: ", elem[1], "\ttext: ", elem[2])

# Monkey patching with Object attributes
########################################
caesar_load(crypter)
crypter.plain_text = 'CRYPTO IS SHORT FOR CRYPTOGRAPHY'
crypter.key = 3
crypter.alphabet = alphabet
string = crypter.cipher()
print("original: \t", crypter.plain_text)
print("ciphered: \t", string)

# Monkey patching with partial attributes
#########################################

string = crypter.cipher(key=crypter.key, alphabet=alphabet)
print("original: \t", crypter.plain_text)
print("ciphered: \t", string)

# Class style
#############

crypter = Caesar()
plain_text = 'QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD'
key = -3
string = crypter.decipher(alphabet, plain_text, key)
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
