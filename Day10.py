def lookAndSay(number):
    """
    Applies the 'look and say' procedure to a given string of numbers.

    Look and say
    ------------
    1 becomes 11 (1 copy of digit 1).
    11 becomes 21 (2 copies of digit 1).
    21 becomes 1211 (one 2 followed by one 1).
    1211 becomes 111221 (one 1, one 2, and two 1s).
    111221 becomes 312211 (three 1s, two 2s, and one 1).

    Parameters
    ----------
    number : str
        Starting string of numbers.

    Returns
    -------
    out : str
        The result of applying the look and say procedure to the starting string.

    """
    i, out = 0, ''
    while i < len(number):
        current_char = number[i]
        current_num = 1
        i += 1
        while i < len(number) and number[i] == current_char:
            current_num += 1
            i += 1
        out += str(current_num) + current_char

    return out

def Day10_Part1(filename='Inputs/Day10_Inputs.txt'):
    """
    Calculates the total length of the resulting string after applying the 'look and say' procedure
    to a starting string given in an input file 40 times.

    Look and say
    ------------
    1 becomes 11 (1 copy of digit 1).
    11 becomes 21 (2 copies of digit 1).
    21 becomes 1211 (one 2 followed by one 1).
    1211 becomes 111221 (one 1, one 2, and two 1s).
    111221 becomes 312211 (three 1s, two 2s, and one 1).

    Parameters
    ----------
    filename : str, optional
        Input file containing the starting string.
        The default is 'Inputs/Day10_Inputs.txt'.

    Returns
    -------
    number_length : int
        The length of the resulting string.

    """
    file = open(filename)
    number = None
    for line in file:
        line = line.strip().split()
        if len(line) > 0:
            number = line[0]
    file.close()

    x, y, ratio = [0], [len(number)], []
    for i in range(40):
        number = lookAndSay(number)
        x.append(i + 1)
        y.append(len(number))
        ratio.append(y[-1]/y[-2])

    number_length = len(number)

    return number_length

from collections.abc import Iterable

def flatten(xs):
    """
    Flattens a given array down to a 1-dimensional generator.

    Parameters
    ----------
    xs : n-dimensional iterable of iterables
        Initial n-dimensional array. Can be uneven.

    Returns
    -------
    x : generator
        The flattened 1-dimensional array as a generator.

    """
    for x in xs:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            yield from flatten(x)
        else:
            yield x

def Day10_Part2(filename='Inputs/Day10_Inputs.txt', elements='Inputs/ConwayElements.txt'):
    """
    Calculates the total length of the resulting string after applying the 'look and say' procedure
    to a starting string given in an input file 50 times, using Conway's element system to simplify
    the problem.

    Look and say
    ------------
    1 becomes 11 (1 copy of digit 1).\n
    11 becomes 21 (2 copies of digit 1).\n
    21 becomes 1211 (one 2 followed by one 1).\n
    1211 becomes 111221 (one 1, one 2, and two 1s).\n
    111221 becomes 312211 (three 1s, two 2s, and one 1).

    Parameters
    ----------
    filename : str, optional
        Input file containing the starting string.
        The default is 'Inputs/Day10_Inputs.txt'.

    elements : str, optional
        Input file containing the names, numbers and decays of the 92 Conway elements.

    Returns
    -------
    number_length : int
        The length of the resulting string.

    """
    file = open(filename)
    number = None
    for line in file:
        line = line.strip().split()
        if len(line) > 0:
            number = line[0]
    file.close()

    elements_file = open(elements)
    element_to_number = {}
    number_to_element = {}
    decays = {}
    for line in elements_file:
        line = line.strip().split()
        if len(line) > 0:
            element_to_number[line[0]] = line[1]
            number_to_element[line[1]] = line[0]
            decays[line[0]] = line[2].split('.')
    elements_file.close()

    sequence = [number_to_element[number]]

    for i in range(50):
        sequence = list(flatten([decays[e] for e in sequence]))

    number_length = sum([len(element_to_number[e]) for e in sequence])

    return number_length
