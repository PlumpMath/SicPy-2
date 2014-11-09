from sicpy.utils.string import strip_duplicates

class Alphabet:
    """
    """
    def __init__(self, string):
        """ """
        self.alpha      = string
        self.length     = len(string)
        self.duplicates = self.check_duplicates()

    def check_length(self):
        """ """
        if len(self.alpha) == self.length:
            self.checked_length = True
            return True
        else:
            self.checked_length = False
            return False

    def check_duplicates(self):
        """ """
        if self.alpha == strip_duplicates(self.alpha):
            self.checked_duplicates = True
            return True
        else:
            self.checked_duplicates = False
            return False
