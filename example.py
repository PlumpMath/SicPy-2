# example

from main             import Cryptobox
from alphabet         import Alphabet
from ciphers.caesar   import caesar_load
from ciphers.vigenere import vigenere_load

crypter = Cryptobox()

alphabet = Alphabet()
alphabet.case_sensitive = True
alphabet.mayus  = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet.minus  = 'abcdefghijklmnopqrstuvwxyz'
alphabet.length = 26

#plain_text = 'Jupiter knows more of all that weird\' stuff'
plain_text = 'Qeb NRFZH YoLTK CLU GRJMP LSBO QEB IXWV ALD'

key = -3
caesar_load()
string = crypter.decipher(alphabet, plain_text, key)
print("original: \t", plain_text)
print("deciphered: \t", string)
print("Now Bruteforce: ")
string = crypter.bruteforce(alphabet, plain_text, 25)
print(string)

print()

plain_text = 'Crypto is short for cryptography'
key = 'ABCD'
vigenere_load()
cipher_text = crypter.cipher(alphabet, plain_text, key)
string = crypter.decipher(alphabet, cipher_text, key)
print("original:\t", plain_text)
print("cipher: \t", cipher_text)
print("decipher:\t", string)

# Just enough to try 'ABCD'
string = crypter.bruteforce(alphabet, cipher_text, 19010)
for elem in string:
    print("key: ", elem[0], "\tde-key: ", elem[1], "\ttext: ", elem[2])
