""" SicPy
"""

# __version__ = '0.1'
# __author__  = 'disrupts'
# __license__ = 'GPLv3'

# Cryptobox should only be used to implement ciphers
#from sicpy.cryptobox import Cryptobox

# Ciphers are imported directly with sicpy
#  not requiring an aditional import
from sicpy.ciphers.caesar     import Caesar
from sicpy.ciphers.vigenere   import Vigenere
from sicpy.ciphers.railfence import RailFence

# Alphabet can be used to build alphabets easily
# >>> myalpha = Alphabet('ABSDE')
from sicpy.alphabet  import Alphabet
# LATIN is imported by cryptobox.py
