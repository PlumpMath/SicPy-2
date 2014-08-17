class Alphabet:
    """
    """
    def __init__(self):
        """ """
        self.case_sensitive     = False
        self.mayus              = ''
        self.minus              = ''
        self.length             = 0
        self.checked_length     = False
        self.checked_duplicates = False
        self.checked            = False

    def check_lengths(self):
        """ """
        if self.case_sensitive == True:
            if len(self.mayus) == len(self.minus) == self.length:
                self.checked_length = True
            else:
                self.checked_length = False
        elif self.case_sensitive == False:
            if self.minus == '' and len(self.mayus) == self.length:
                self.checked_length = True
            else:
                self.checked_length = False
        else:
            self.checked_length = False

    def check_duplicates(self):
        """ """
        if self.alphabet.mayus == self.strip_duplicates(self.alphabet.mayus) \
          and                                                                \
          self.alphabet.minus == self.strip_duplicates(self.alphabet.minus):
            self.checked_duplicates = True
        else:
            self.checked_duplicates = False

    def check(self):
        """ """
        self.check_lengths()
        self.check_duplicates()

    def mayus(self, string):
        """ """
        self.mayus = string
        self.length = len(string)
        self.check()

    def minus(self, string):
        """ """
        self.minus = string
        self.length = len(string)
        self.check()

    def strip_duplicates(self,string):
        """ """
        stripped = ''
        for letter in string:
            if letter not in (self.alphabet.minus + self.alphabet.minus):
                stripped += letter
            elif i not in n:
                stripped += letter

