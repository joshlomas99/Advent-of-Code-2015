def Day16_Part1(filename='Inputs/Day16_Inputs.txt',
                result={'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0,
                        'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}):
    """
    Determine the number (out of 500) of the Aunt Sue whose properties given in an input file match
    with those output by a My First Crime Scene Analysis Machine (MFCSAM) when applied to the
    wrapping paper from a gift given to you by a mystery Aunt Sue.

    Parameters
    ----------
    filename : str, optional
        Input file containing the numbered Sues and their properties.
        The default is 'Inputs/Day16_Inputs.txt'.
    
    result : dict(str: int), optional
        The properties of the mystery Aunt Sue output by the MFCSAM.
        The default is {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0,
                        'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}

    Returns
    -------
    sue_number : int
        The number of the mystery Aunt Sue.

    """
    file = open(filename)
    sues = []
    result_items = result.items()
    for line in file:
        line = line.strip().split()
        if len(line) > 0:
            sues.append({line[2*n][:-1]: int(line[2*n+1].split(',')[0]) for n in range(1, int(len(line)/2))})
            if all(item in result_items for item in sues[-1].items()):
                file.close()
                sue_number = len(sues)
                return sue_number

    file.close()
    return None

def Day16_Part2(filename='Inputs/Day16_Inputs.txt',
                result={'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0,
                        'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}):
    """
    Determine the number (out of 500) of the Aunt Sue whose properties given in an input file match
    with those output by a My First Crime Scene Analysis Machine (MFCSAM) when applied to the
    wrapping paper from a gift given to you by a mystery Aunt Sue. However, it turns out that the
    cats and trees readings from the MFCSAM indicates that there are greater than that many (due
    to the unpredictable nuclear decay of cat dander and tree pollen), while the pomeranians and
    goldfish readings indicate that there are fewer than that many (due to the modial interaction
    of magnetoreluctance).

    Parameters
    ----------
    filename : str, optional
        Input file containing the numbered Sues and their properties.
        The default is 'Inputs/Day16_Inputs.txt'.
    
    result : dict(str: int), optional
        The properties of the mystery Aunt Sue output by the MFCSAM.
        The default is {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0,
                        'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}

    Returns
    -------
    sue_number : int
        The number of the mystery Aunt Sue given the new conditions.

    """
    file = open(filename)
    sues = []
    for line in file:
        line = line.strip().split()
        if len(line) > 0:
            sues.append({line[2*n][:-1]: int(line[2*n+1].split(',')[0]) for n in \
                         range(1, int(len(line)/2))})
            if all(sues[-1][i] > result[i] if i in ['cats', 'trees'] else sues[-1][i] < result[i] \
                   if i in ['pomeranians', 'goldfish'] else sues[-1][i] == result[i] for i in \
                       sues[-1]):
                file.close()
                return len(sues)

    file.close()
    return None
