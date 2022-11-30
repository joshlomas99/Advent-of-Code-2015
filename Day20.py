def factors(n):
    """
    Finds all the factors of an integer n.

    Parameters
    ----------
    n : int
        Number to find the factors of.

    Returns
    -------
    f : set
        All the factors of n.

    """
    # Initialise set of factors.
    f = set()
    # Can skip even factors for odd numbers
    step = 2 if n%2 else 1
    # Test each integer from 1 to sqrt(n)
    for i in range(1, int((n)**0.5)+1, step):
        if n%i == 0: # If i goes into n with no remainder
            # Add i and n/i as both are factors
            f.add(i)
            f.add(int(n/i))
    return f

def Day20_Part1(filename='Inputs/Day20_Inputs.txt'):
    """
    Calculates the lowest house number to get at least as many presents as the value given in an
    input file. Presents are delivered to infinitely many houses by infinitely many elves numbered
    1, 2, 3, etc., that deliver presents according to their number:
        - The first Elf (number 1) delivers presents to every house: 1, 2, 3, 4, 5...
        - The second Elf (number 2) delivers presents to every second house: 2, 4, 6, 8, 10...
        - Elf number 3 delivers presents to every third house: 3, 6, 9, 12, 15...
    And each Elf delivers presents equal to ten times his or her number at each house.

    Parameters
    ----------
    filename : str, optional
        Input file giving the present limit to be found.
        The default is 'Inputs/Day20_Inputs.txt'.

    Returns
    -------
    house_num : int
        The lowest house number to get at least as many presents as the value given in the input
        file.

    """
    # Parse input file
    min_presents = int(list(open(filename))[0])

    house_num = 1
    # Each elf visits every house whose number is a multiple of the elf's number
    # So the total presents at a house are equal to 10 times the sum of the factors of the house
    # number
    while 10*sum(factors(house_num)) < min_presents:
        house_num += 1

    return house_num

def factors_to_50(n):
    """
    Finds the factors i of an integer n such that n/i <= 50.

    Parameters
    ----------
    n : int
        Number to find the factors of.

    Returns
    -------
    f : set
        All the factors of n such that n/i <= 50.

    """
    # Initialise set of factors.
    f = set()
    # Can skip even factors for odd numbers
    step = 2 if n%2 else 1
    # Test each integer from 1 to 50
    for i in range(1, 51, step):
        if n%i == 0: # If i goes into n with no remainder
            # Add n/i to set
            f.add(int(n/i))
    return f

def Day20_Part2(filename='Inputs/Day20_Inputs.txt'):
    """
    Calculates the lowest house number to get at least as many presents as the value given in an
    input file. Presents are delivered to infinitely many houses by infinitely many elves numbered
    1, 2, 3, etc., that deliver presents according to their number:
        - The first Elf (number 1) delivers presents to every house: 1, 2, 3, 4, 5...
        - The second Elf (number 2) delivers presents to every second house: 2, 4, 6, 8, 10...
        - Elf number 3 delivers presents to every third house: 3, 6, 9, 12, 15...
    And each elf delivers presents equal to eleven times their number at the first 50 houses they
    visit and then stop.

    Parameters
    ----------
    filename : str, optional
        Input file giving the present limit to be found.
        The default is 'Inputs/Day20_Inputs.txt'.

    Returns
    -------
    house_num : int
        The lowest house number to get at least as many presents as the value given in the input
        file.

    """
    # Parse input file
    min_presents = int(list(open(filename))[0])

    house_num = 1
    # Each elf visits every house whose number is a multiple of the elf's number by a number less
    # than or equal to 50
    # So the total presents at a house are equal to 11 times the sum of the factors i of the house
    # number n such that n/i <= 50
    while 11*sum(factors_to_50(house_num)) < min_presents:
        house_num += 1

    return house_num
