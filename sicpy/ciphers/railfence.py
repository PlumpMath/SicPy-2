from sicpy.cryptobox import Cryptobox
from sicpy.utils.iterators import integer_iterator

class RailFence(Cryptobox):
    """ Rail-fence Sawtooth
    """
    # DOES NOT NEED ALPHASBET
    def __init__(self, alphabet=None, key=None, plain_text=None,
                 cipher_text=None):
        """ """
        Cryptobox.__init__(self, alphabet, key, plain_text, cipher_text)
        self.key_init = 2

    def cipher(self, alphabet=None, input_text=None, key=None):
        """ """

        # Variable inference
        if alphabet == None:
            alphabet = self.alphabet
        if input_text == None:
            input_text = self.plain_text
        if key == None:
            key = self.key

        # Let's make a matrix out of the original text
        text_length = len(input_text)
        buffer_matrix = [[0 for i in range(key)] for j in range(text_length)]
        rail_list = generate_rail_list(key, text_length)
        for position, letter in enumerate(input_text):
            buffer_matrix[position][rail_list[position]] = letter

        # Let's transpose the matrix
        matrix_width = len(buffer_matrix[0])
        buffer_matrix = (
          [[row[i] for row in buffer_matrix] for i in range(matrix_width)] )

        # Now let's flatten the matrix to a single vector
        buffer_list = sum(buffer_matrix,[])

        # change to string omiting 0s
        output_text = ''
        for letter in buffer_list:
            if letter != 0:
                output_text += str(letter)

        return output_text

    def decipher(self, alphabet=None, key=None, input_text=None):
        """
        asimetrical algo, decipher is different
        (thow known and unique for each cipher)
        """

        # Variable inference
        if alphabet == None:
            alphabet = self.alphabet
        if input_text == None:
            input_text = self.cipher_text
        if key == None:
            key = self.key

        # make a matrix with filled with 0 and 1, 1 representing
        # the place were letters will be placed
        text_length = len(input_text)
        buffer_matrix = [[0 for i in range(key)] for j in range(text_length)]
        rail_list = generate_rail_list(key, text_length)
        for position, letter in enumerate(input_text):
            buffer_matrix[position][rail_list[position]] = 1

        # place letters (line per line)
        position = 0
        for j in range(key):
            for i in range(len(buffer_matrix)):
                if buffer_matrix[i][j] == 1:
                    buffer_matrix[i][j] = input_text[position]
                    position += 1

        # Read (extract) letters (one letter per column)
        output_text = ''
        for i in range(len(buffer_matrix)):
            for j in range(key):
                #if isinstance(buffer_matrix[i][j],int):
                if buffer_matrix[i][j] != 0:
                    output_text += buffer_matrix[i][j]

        return output_text

    def bruteforce(self, times=None, alphabet=None, input_text=None):
        """
        times should be lower than len(input_text)
        """
        # initialise times to maximum possible value
        if times == None:
            times = len(input_text) - 1

        return Cryptobox.bruteforce(self, times, alphabet, input_text)

    def key_inverse(self, alphabet=None, key=None):
        """ algo is asimetric, same key is used, just returns same key """
        # Variable inference
        if alphabet == None:
            alphabet = self.alphabet
        if key == None:
            key = self.key
        # Main code
        return key

    def key_iterate(self, alphabet=None, key=None):
        """
        need to pass alphabet for consistency"""

        # Variable inference
        #if alphabet == None:
        #    alphabet = self.alphabet
        if key == None:
            key = self.key
        # Main code
        return key + 1 # the length of the alphabet is not the limit

def generate_rail_list(key, list_length):
    """ Generates a list of integers following a sawtooth or rail fence
    """
    return_list = []
    element     = 0
    for whatever in range(list_length):
        return_list.append(element)
        # Change direction
        if element == (key-1):
            dir_up = False
        if element == 0:
            dir_up = True
        # Update element
        if dir_up == True:
            element += 1
        else:
            element -= 1
    return return_list
