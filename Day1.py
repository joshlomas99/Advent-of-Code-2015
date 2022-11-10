def Day1_Part1(filename='Inputs/Day1_Inputs.txt'):
    """
    Calculate the floor reached at the end of a series of instructions given in an input
    file, where '(' means go up a floor and ')' means go down a floor, starting at floor
    0.

    Parameters
    ----------
    filename : str, optional
        Input file providing the instructions.
        The default is 'Inputs/Day1_Inputs.txt'.

    Returns
    -------
    floor : int
        Final floor number.

    """
    file = open(filename)
    for line in file:
        line = line.strip().split()
        line = line
        if len(line) > 0:
            parentheses = line[0]
    file.close()

    floor = parentheses.count('(') - parentheses.count(')')
            
    return floor

def Day1_Part2(filename='Inputs/Day1_Inputs.txt'):
    """
    Calculate the position of the instruction which first causes the floor to become -1,
    while moving according to a series of instructions given in an input file, where
    '(' means go up a floor and ')' means go down a floor, starting at floor 0.

    Parameters
    ----------
    filename : str, optional
        Input file providing the instructions.
        The default is 'Inputs/Day1_Inputs.txt'.

    Returns
    -------
    position : int
        Position of the first instruction which causes the floor to go below 0.

    """
    file = open(filename)
    parentheses = []
    for line in file:
        line = line.strip().split()
        if len(line) > 0:
            parentheses.append(line[0])
    file.close()

    floor = 0
    for n, parenthesis in enumerate(parentheses[0]):
        if parenthesis == '(':
            floor += 1
        elif parenthesis == ')':
            floor -= 1
        if floor == -1:
            position = n+1
            return position
        