def totalHappiness(arrangement, pairings):
    """
    Calculates the total happiness of an arrangement of members given the happiness gained/lost
    by each person depending on who they are next to.

    Parameters
    ----------
    arrangement : list of str
        List of members in a given arrangement.
    pairings : dict(str : dict(str : int))
        The happiness of each member when seated next to every other member.

    Returns
    -------
    happiness : int
        The total happiness of the group in the given arrangement.

    """
    happiness = 0
    for i in range(len(arrangement)):
        happiness += pairings[arrangement[i]][arrangement[(i+1)%len(arrangement)]]
        happiness += pairings[arrangement[(i+1)%len(arrangement)]][arrangement[i]]

    return happiness

from itertools import permutations

def Day13_Part1(filename='Inputs/Day13_Inputs.txt'):
    """
    Calculates the seating arrangement of members in a group which maximises the total happiness
    of the group, where the happiness gained/lost by each person depending on who they are next to
    is given in an input file.

    Parameters
    ----------
    filename : str, optional
        Input file containing the happiness of each pairing.
        The default is 'Inputs/Day13_Inputs.txt'.

    Returns
    -------
    opt_arrangement : list of str
        The optimum arrangement of members which maximises the happiness of the group.
    opt_happiness : int
        The total happiness of the group in the optimal arrangement.

    """
    file = open(filename)
    pairings = {}
    for line in file:
        line = line.strip().split()
        if len(line) > 0:
            if line[0] in pairings:
                pairings[line[0]][line[-1][:-1]] = int(line[3])*(1 - (2*(line[2] == 'lose')))
            else:
                pairings[line[0]] = {line[-1][:-1] : int(line[3])*(1 - (2*(line[2] == 'lose')))}
    file.close()

    lastSeat = list(pairings.keys())[-1]
    opt_arrangement, opt_happiness = None, 0

    for arrangement in permutations(list(pairings.keys())[:-1]):
        arrangement = list(arrangement)
        arrangement.append(lastSeat)
        happiness = totalHappiness(arrangement, pairings)
        if opt_arrangement == None or happiness > opt_happiness:
            opt_arrangement = arrangement.copy()
            opt_happiness = 1*happiness

    return opt_arrangement, opt_happiness

def Day13_Part2(filename='Inputs/Day13_Inputs.txt'):
    """
    Calculates the seating arrangement of members in a group which maximises the total happiness
    of the group, where the happiness gained/lost by each person depending on who they are next to
    is given in an input file and an additional person "Me" is added who has no change in happiness
    for themselves or anyone else when they sit together.

    Parameters
    ----------
    filename : str, optional
        Input file containing the happiness of each pairing.
        The default is 'Inputs/Day13_Inputs.txt'.

    Returns
    -------
    opt_arrangement : list of str
        The optimum arrangement of members which maximises the happiness of the group.
    opt_happiness : int
        The total happiness of the group in the optimal arrangement.

    """
    file = open(filename)
    pairings = {}
    for line in file:
        line = line.strip().split()
        if len(line) > 0:
            if line[0] in pairings:
                pairings[line[0]][line[-1][:-1]] = int(line[3])*(1 - (2*(line[2] == 'lose')))
            else:
                pairings[line[0]] = {line[-1][:-1] : int(line[3])*(1 - (2*(line[2] == 'lose')))}
    file.close()

    me_dict = {key:0 for key in pairings.keys()}
    for key in pairings.keys():
        pairings[key]['Me'] = 0
    pairings['Me'] = me_dict.copy()

    lastSeat = list(pairings.keys())[-1]
    opt_arrangement, opt_happiness = None, 0

    for arrangement in permutations(list(pairings.keys())[:-1]):
        arrangement = list(arrangement)
        arrangement.append(lastSeat)
        happiness = totalHappiness(arrangement, pairings)
        if opt_arrangement == None or happiness > opt_happiness:
            opt_arrangement = arrangement.copy()
            opt_happiness = 1*happiness

    return opt_arrangement, opt_happiness
