import numpy as np

def minKey(dictionary):
    return list(dictionary.keys())[np.argmin(list(dictionary.values()))], min(list(dictionary.values()))

def Day9_Part1(filename='Inputs/Day9_Inputs.txt'):
    """
    Calculates the shortest possible route between a set of locations while visiting each location
    exactly once, given the distances between every location in an input file.

    Parameters
    ----------
    filename : str, optional
        Input file containing the distances between locations.
        The default is 'Inputs/Day9_Inputs.txt'.

    Returns
    -------
    shortest_route : list of str
        The shortest route through every location in order.
    shortest_distance : int
        The length of the shortest route through every location.

    """
    file = open(filename)
    distances = {}
    min_route = None
    for line in file:
        line = line.strip().split(' -> ')
        if len(line) > 0:
            route, dist = line[0].split(' = ')
            route = route.split(' to ')
            for i in [0, 1]:
                if route[i] in distances:
                    distances[route[i]][route[(i+1)%2]] = int(dist)
                else:
                    distances[route[i]] = {route[(i+1)%2] : int(dist)}
            if not min_route or min_route[1] > int(dist):
                min_route = [route, int(dist)]
    file.close()

    shortest_route = min_route[0]
    shortest_distance = min_route[1]

    for i in [0, 1]:
        distances[shortest_route[i]].pop(shortest_route[(i+1)%2])

    while len(shortest_route) < len(distances):
        if minKey(distances[shortest_route[-1]])[1] < minKey(distances[shortest_route[0]])[1]:
            next_loc, next_dist = minKey(distances[shortest_route[-1]])

            distances[shortest_route[-1]] = {}
            for loc in distances:
                distances[loc].pop(shortest_route[-1], None)

            shortest_route.append(next_loc)
            shortest_distance += next_dist

            for i in [0, -1]:
                distances[shortest_route[i]].pop(shortest_route[(i+1)%-2], None)

        else:
            next_loc, next_dist = minKey(distances[shortest_route[0]])

            distances[shortest_route[0]] = {}
            for loc in distances:
                distances[loc].pop(shortest_route[0], None)

            shortest_route = [next_loc] + shortest_route
            shortest_distance += next_dist

            for i in [0, -1]:
                distances[shortest_route[i]].pop(shortest_route[(i+1)%-2], None)

    return shortest_route, shortest_distance

from itertools import permutations

def Day9_Part1a(filename='Inputs/Day9_Inputs.txt'):
    """
    Calculates the shortest possible route between a set of locations while visiting each location
    exactly once, given the distances between every location in an input file.

    Parameters
    ----------
    filename : str, optional
        Input file containing the distances between locations.
        The default is 'Inputs/Day9_Inputs.txt'.

    Returns
    -------
    shortest_route : list of str
        The shortest route through every location in order.
    shortest_distance : int
        The length of the shortest route through every location.

    """
    file = open(filename)
    distances = {}
    for line in file:
        line = line.strip().split(' -> ')
        if len(line) > 0:
            route, dist = line[0].split(' = ')
            route = route.split(' to ')
            for i in [0, 1]:
                if route[i] in distances:
                    distances[route[i]][route[(i+1)%2]] = int(dist)
                else:
                    distances[route[i]] = {route[(i+1)%2] : int(dist)}
    file.close()

    shortest_route, shortest_distance = None, 1000

    for route in permutations(distances):
        dist = 0
        for i in range(len(route) - 1):
            dist += distances[route[i]][route[i+1]]
        if dist < shortest_distance:
            shortest_route, shortest_distance = route, dist

    return list(shortest_route), shortest_distance

def Day9_Part2(filename='Inputs/Day9_Inputs.txt'):
    """
    Calculates the longest possible route between a set of locations while visiting each location
    exactly once, given the distances between every location in an input file.

    Parameters
    ----------
    filename : str, optional
        Input file containing the distances between locations.
        The default is 'Inputs/Day9_Inputs.txt'.

    Returns
    -------
    longest_route : list of str
        The longest route through every location in order.
    longest_distance : int
        The length of the longest route through every location.

    """
    file = open(filename)
    distances = {}
    for line in file:
        line = line.strip().split(' -> ')
        if len(line) > 0:
            route, dist = line[0].split(' = ')
            route = route.split(' to ')
            for i in [0, 1]:
                if route[i] in distances:
                    distances[route[i]][route[(i+1)%2]] = int(dist)
                else:
                    distances[route[i]] = {route[(i+1)%2] : int(dist)}
    file.close()

    longest_route, longest_distance = None, 0

    for route in permutations(distances):
        dist = 0
        for i in range(len(route) - 1):
            dist += distances[route[i]][route[i+1]]
        if dist > longest_distance:
            longest_route, longest_distance = route, dist

    return list(longest_route), longest_distance
