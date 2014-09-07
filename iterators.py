def integer_iterator(self, key):
    """ """
    return key + 1

def alphabet_iterator(self, alphabet, key):
    """ """
    length            = len(key)
    last_key_letter   = key[length - 1]
    last_alpha_letter = alphabet.alpha[alphabet.length - 1]
    compare_string    = length * last_alpha_letter
    #print("compare: ", compare_string, " key: ", key) # DEBUG
    if compare_string == key:
        # new cycle!
        new_key = (length + 1) * alphabet.alpha[0]
    else:
        # one letter increments & all the letters change to the right to A
        #pos_to_change = length - 1
        pos_to_change = 0
        for i in range(length - 1, 0, -1):
            #print('posible pos to change to', i) # DEBUG
            if key[i] != last_alpha_letter:
                pos_to_change = i
                break
        pos_in_alpha = alphabet.alpha.find(key[pos_to_change])
        if pos_in_alpha == alphabet.length - 1:
            pos_in_alpha = -1
        new_key = key[:(pos_to_change)] + alphabet.alpha[pos_in_alpha + 1] \
                + (length - pos_to_change - 1) * alphabet.alpha[0]
    return new_key
