def strip_duplicates(string):
        """ """
        stripped = ''
        for letter in string:
            if letter not in stripped:
                stripped += letter
        return stripped

SYMBOLS = ' ¡!¿?-_.,:;()[]{}+*=/|\\ºª\'"@\#$%&'
