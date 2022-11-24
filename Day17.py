from itertools import combinations

def Day17_Part1(filename='Inputs/Day17_Inputs.txt', total=150):
    """
    Calculates the number of different combinations of the containers given in an input file which
    will hold exactly a specified volume of eggnog.

    Parameters
    ----------
    filename : str, optional
        Input file giving the sizes of the different containers.
        The default is 'Inputs/Day17_Inputs.txt'.
    
    total : int, optional
        The total volume of eggnog.
        The default is 150 litres.

    Returns
    -------
    num_combinations : int
        The number of combinations of the containers with the correct total volume.

    """
    file = open(filename)
    containers = []
    for line in file:
        line = line.strip().split()
        if len(line) > 0:
            containers.append(int(line[0]))
    file.close()

    num_combinations = sum([sum(comb) == total for r in range(1, len(containers)+1) \
                            for comb in combinations(containers, r)])

    return num_combinations

def Day17_Part2(filename='Inputs/Day17_Inputs.txt', total=150):
    """
    Calculates the number of different combinations of the containers given in an input file which
    will hold exactly a specified volume of eggnog, while using the fewest possible containers.

    Parameters
    ----------
    filename : str, optional
        Input file giving the sizes of the different containers.
        The default is 'Inputs/Day17_Inputs.txt'.
    
    total : int, optional
        The total volume of eggnog.
        The default is 150 litres.

    Returns
    -------
    num_combinations : int
        The number of combinations of the containers with the correct total volume, while using
        the fewest possible containers.

    """
    file = open(filename)
    containers = []
    for line in file:
        line = line.strip().split()
        if len(line) > 0:
            containers.append(int(line[0]))
    file.close()

    for r in range(1, len(containers)+1):
        possibilities = [sum(comb) == total for comb in combinations(containers, r)]
        if any(possibilities):
            num_combinations = sum(possibilities)
            return num_combinations
