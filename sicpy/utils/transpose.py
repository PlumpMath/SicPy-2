def transpositions(sentence):
    """ Generate all possible transposition of a given text

    This funcion takes a string and will give back a list of string,
    which are all the possible resulst of transposition ciphers
    - or posible plain text if called on a transposed cipher text.

    You will end up with a list with as many elements as:
    >>> math.factorial(len(your_string))

    The rate of growth of the factorial ends up being faster than
    exponentials. Beware of the length of your string.
    If your string is longer than a few char it will resource intensive
    and will take a while to execute.

    If letters are repeated in the original string, the transposition
    function will return repeated transpositions.
    The easiest way to filter them is to create a set out of them:
    >>> set(transpositions(your_string))

    And if you'd like to have a shorter list instead of a set, just call
    list() on in. You can even nest them as such:
    >>> list(set(transpositions(your_string))

    This function has a big overhead as it changes the generator into
    a list. If you'd rather have the generator don't call enumerate
    or anything on the result of this function.
    Use itertools.permutations directly as such:
    >>> itertools.permutations(your_string)
    """

    import itertools
    permutations = itertools.permutations(sentence)
    all_perms = []
    for tupl in permutations:
        string = ''
        for letter in tupl:
            string += str(letter)
        all_perms.append(string)
    return all_perms
