def countInts(iterable, count=0):
    """
    Calculates the sum of all numbers in an iterable which can contain other iterables (list or
    dict), strings or numbers. Iterables within iterables can contain further iterables and so on.

    Parameters
    ----------
    iterable : list or dict
        The iterable to be parsed.

    count : int, optional
        The starting value of the number sum, required for recursion.
        Default is 0.

    Returns
    -------
    count : int
        The final sum of all numbers within the iterable.

    """
    if type(iterable) == list:
        for item in iterable:
            if type(item) in [list, dict]:
                count = countInts(item, count)
            elif type(item) == int:
                count += item

    elif type(iterable) == dict:
        for item in iterable.values():
            if type(item) in [list, dict]:
                count = countInts(item, count)
            elif type(item) == int:
                count += item

    return count

def Day12_Part1(filename='Inputs/Day12_Inputs.txt'):
    """
    Calculates the sum of all numbers in an iterable, given in an input file, which can contain
    other iterables (list or dict), strings or numbers. Iterables within iterables can contain
    further iterables and so on.

    Parameters
    ----------
    filename : str, optional
        Input file containing the iterable.
        The default is 'Inputs/Day12_Inputs.txt'.

    Returns
    -------
    count : int
        The final sum of all numbers within the iterable.

    """
    file = open(filename)
    for line in file:
        line = line.strip().split()
        if len(line) > 0:
            json = eval(line[0])
    file.close()

    count = countInts(json, 0)

    return count

def countInts_noRed(iterable, count):
    """
    Calculates the sum of all numbers in an iterable which can contain other iterables (list or
    dict), strings or numbers. Iterables within iterables can contain further iterables and so on.
    However, any dict which contains the value 'red' should be ignored completely in the sum.

    Parameters
    ----------
    iterable : list or dict
        The iterable to be parsed.

    count : int, optional
        The starting value of the number sum, required for recursion.
        Default is 0.

    Returns
    -------
    count : int
        The final sum of all numbers within the iterable.

    """
    if type(iterable) == list:
        for item in iterable:
            if type(item) in [list, dict]:
                count = countInts_noRed(item, count)
            elif type(item) == int:
                count += item

    elif type(iterable) == dict:
        if 'red' in iterable.values():
            return count
        for item in iterable.values():
            if type(item) in [list, dict]:
                count = countInts_noRed(item, count)
            elif type(item) == int:
                count += item

    return count

def Day12_Part2(filename='Inputs/Day12_Inputs.txt'):
    """
    Calculates the sum of all numbers in an iterable, given in an input file, which can contain
    other iterables (list or dict), strings or numbers. Iterables within iterables can contain
    further iterables and so on. However, any dict which contains the value 'red' should be ignored
    completely in the sum.

    Parameters
    ----------
    filename : str, optional
        Input file containing the iterable.
        The default is 'Inputs/Day12_Inputs.txt'.

    Returns
    -------
    count : int
        The final sum of all numbers within the iterable.

    """
    file = open(filename)
    for line in file:
        line = line.strip().split()
        if len(line) > 0:
            json = eval(line[0])
    file.close()

    count = countInts_noRed(json, 0)

    return count
