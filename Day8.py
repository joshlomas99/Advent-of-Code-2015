def Day8_Part1(filename='Inputs/Day8_Inputs.txt'):
    """
    Calculates the difference between the number of characters in the code representation of a set
    of encoded string literals given in an input file and the number of characters in the string
    once it is in-memory.

    Parameters
    ----------
    filename : str, optional
        Input file containing the encoded strings.
        The default is 'Inputs/Day8_Inputs.txt'.

    Returns
    -------
    diff : int
        The difference between the number of characters.

    """
    file = open(filename)
    code_chars = 0
    mem_chars = 0
    for line in file:
        line = line.strip().split(' -> ')
        if len(line) > 0:
            code_chars += len(line[0])
            mem_chars += len(eval(line[0]))
    file.close()

    diff = code_chars - mem_chars

    return diff

def Day8_Part2(filename='Inputs/Day8_Inputs.txt'):
    """
    Calculates the difference between the number of characters in the code representation of a set
    of encoded string literals given in an input file and the number of characters in each code
    representation once encoded as a new string.

    Parameters
    ----------
    filename : str, optional
        Input file containing the encoded strings.
        The default is 'Inputs/Day8_Inputs.txt'.

    Returns
    -------
    diff : int
        The difference between the number of characters.

    """
    file = open(filename)
    orig_chars = 0
    encoded_chars = 0
    for line in file:
        line = line.strip().split(' -> ')
        if len(line) > 0:
            orig_chars += len(line[0])
            for char in line[0]:
                if char.isalnum():
                    encoded_chars += 1
                else:
                    encoded_chars += 2
            encoded_chars += 2
    file.close()

    diff = encoded_chars - orig_chars

    return diff
