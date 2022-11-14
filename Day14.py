def Day14_Part1(filename='Inputs/Day14_Inputs.txt'):
    """
    Calculates the maximum distance reached after 2503 seconds out of a group of reindeer who can
    travel at a given speed for a given time before needing a given rest period to continue moving,
    as given in an input file.

    Parameters
    ----------
    filename : str, optional
        Input file containing the happiness of each pairing.
        The default is 'Inputs/Day14_Inputs.txt'.

    Returns
    -------
    winning_distance : int
        The maximum distance reached out of the reindeer.

    """
    file = open(filename)
    reindeers = {}
    for line in file:
        line = line.strip().split()
        if len(line) > 0:
            reindeers[line[0]] = {'Speed': int(line[3]), 'Fly Time': int(line[6]),
                                 'Rest Time': int(line[-2]), 'Distance': 0,
                                 'Step Time': int(line[6]) + int(line[-2])}

    file.close()

    seconds = 0
    while seconds < 2503:
        for reindeer in reindeers:
            if seconds%reindeers[reindeer]['Step Time'] < reindeers[reindeer]['Fly Time']:
                reindeers[reindeer]['Distance'] += reindeers[reindeer]['Speed']
        seconds += 1

    winning_distance = max([reindeers[reindeer]['Distance'] for reindeer in reindeers])

    return winning_distance

def Day14_Part2(filename='Inputs/Day14_Inputs.txt'):
    """
    Calculates the maximum points earned after 2503 seconds out of a group of reindeer who can
    travel at a given speed for a given time before needing a given rest period to continue moving,
    as given in an input file, where a point is given after every second to the reindeer which have
    travelled the maximum distance so far.

    Parameters
    ----------
    filename : str, optional
        Input file containing the happiness of each pairing.
        The default is 'Inputs/Day14_Inputs.txt'.

    Returns
    -------
    winning_distance : int
        The maximum points earned out of the reindeer.

    """
    file = open(filename)
    reindeers = {}
    for line in file:
        line = line.strip().split()
        if len(line) > 0:
            reindeers[line[0]] = {'Speed': int(line[3]), 'Fly Time': int(line[6]),
                                 'Rest Time': int(line[-2]), 'Distance': 0,
                                 'Step Time': int(line[6]) + int(line[-2]), 'Points': 0}

    file.close()

    seconds = 0
    while seconds < 2503:
        top_dist = []
        for reindeer in reindeers:
            if seconds%reindeers[reindeer]['Step Time'] < reindeers[reindeer]['Fly Time']:
                reindeers[reindeer]['Distance'] += reindeers[reindeer]['Speed']
            if len(top_dist) == 0 or reindeers[reindeer]['Distance'] == reindeers[top_dist[-1]]['Distance']:
                top_dist.append(reindeer)
            elif reindeers[reindeer]['Distance'] > reindeers[top_dist[-1]]['Distance']:
                top_dist = [reindeer]

        for reindeer in top_dist:
            reindeers[reindeer]['Points'] += 1

        seconds += 1

    winning_points = max([reindeers[reindeer]['Points'] for reindeer in reindeers])

    return winning_points
