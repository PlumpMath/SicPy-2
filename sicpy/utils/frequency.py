def frequencies(alphabet=None, dictionary=None, text=None, length=1):
    """

    without alphabet, just pick a group of that length
    with alphabet, pick groups made only of valid characters
    """

    # Input errors
    if text is None or length > len(text):
        return None

    # good dictionary initialisation
    if dictionary == None:
        dictionary = {}

    for index in range(len(text) - length + 1):
        # get the substring
        if alphabet is None:
            string = text[(index):(index+length)]

        # string generation if part of alphabet
        else:
            # if first element is not in alphabet, continue
            if alphabet.alpha.find(text[index]) is -1:
                continue
            # if it isn't, it is a valid subchar
            new_index = index
            string    = ''
            counter   = 0
            while counter < length:
                # if there aren't any more valid chars, we need to finish
                if new_index+length > len(text):
                    break
                char = text[new_index]
                if alphabet.alpha.find(char) is not -1:
                    string  += char
                    counter += 1
                new_index += 1

        # update dictionary
        if dictionary.get(string) is None:
            dictionary.setdefault(string, 1)
        else:
            dictionary[string] += 1

    return dictionary


def frequencies_in_range(alphabet=None, dictionary=None, text=None,
                         start=1, stop=None, step=1):
    """

    SET AS start included, stop excluded, just as range()
    """

    # set default values
    if dictionary == None:
        dictionary = {}
    if stop == None:
        stop = start + 1

    # Input errors from the range
    if start < 1 or start >= stop or stop < 1 or step < 1:
        return None

    for length in range(start, stop, step):
        frequencies(alphabet, dictionary, text, length)

    return dictionary


def dict_to_list(dictionary):
    return [x for x in dictionary.items()]

def sort_list(unsoted_list):
    return sorted(unsoted_list, key=lambda x: x[1], reverse=True)

def frequency_dict_to_list(dictionary):
    return sort_list(dict_to_list(dictionary))
