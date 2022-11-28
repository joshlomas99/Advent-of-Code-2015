import numpy as np
import matplotlib.pyplot as plt

def Day18_Part1(filename='Inputs/Day18_Inputs.txt', steps=100, animate=False):
    """
    Calculates the number lights in a grid that are still on after a given number of applications
    of a set of rules, with the initial state of the lights given in an input file.

    Rules
    -----
    The state a light should have next is based on its current state (on or off) plus the number
    of neighbors that are on:
        - A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
        - A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.
    All of the lights update simultaneously; they all consider the same current state before
    moving to the next.
    Lights on the edge of the grid might have fewer than eight neighbors; the missing ones always
    count as "off".

    Parameters
    ----------
    filename : str, optional
        Input file giving the initial state of the lights
        The default is 'Inputs/Day18_Inputs.txt'.
    
    steps : int, optional
        The number of times to apply the rules to the initial state of the lights.
        The default is 100.

    animate : bool
        Whether or not to animate the evolution of the grid of lights by plotting a colour map
        after each step.

    Returns
    -------
    num_on : int
        The number of lights which are on after the given number of steps.

    """
    file = open(filename)
    lights = []
    for line in file:
        line = line.strip().split()
        if len(line) > 0:
            lights.append([1 if l == '#' else 0 for l in line[0]])
    file.close()

    lights = np.array(lights)
    full_row, full_column = lights.shape

    for step in range(steps):
        new_lights = lights.copy()
        for row in range(full_row):
            for column in range(full_column):
                surroundings = [lights[n, m] for n in range(row-1, row+2) \
                                for m in range(column-1, column+2) if not (n == row and m == column) \
                                and n >= 0 and n < full_row and m >= 0 and m < full_column]
                if lights[row, column]:
                    if sum(surroundings) not in [2, 3]:
                        new_lights[row, column] = 0
                else:
                    if sum(surroundings) == 3:
                        new_lights[row, column] = 1
        lights = new_lights.copy()
        if animate:
            plt.imshow(lights,cmap='gray')
            plt.text(99-(9*len(str(step+1))), 10, str(step+1), {'color': 'r', 'fontsize': 25, 'fontweight': 'bold'})
            plt.show()

    num_on = lights.sum()

    return num_on

def Day18_Part2(filename='Inputs/Day18_Inputs.txt', steps=100, animate=False):
    """
    Calculates the number lights in a grid that are still on after a given number of applications
    of a set of rules, with the initial state of the lights given in an input file. However, the
    4 lights in the corners of the grid are now stuck on.

    Rules
    -----
    The state a light should have next is based on its current state (on or off) plus the number
    of neighbors that are on:
        - A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
        - A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.
    All of the lights update simultaneously; they all consider the same current state before
    moving to the next.
    Lights on the edge of the grid might have fewer than eight neighbors; the missing ones always
    count as "off".

    Parameters
    ----------
    filename : str, optional
        Input file giving the initial state of the lights
        The default is 'Inputs/Day18_Inputs.txt'.
    
    steps : int, optional
        The number of times to apply the rules to the initial state of the lights.
        The default is 100.

    animate : bool
        Whether or not to animate the evolution of the grid of lights by plotting a colour map
        after each step.

    Returns
    -------
    num_on : int
        The number of lights which are on after the given number of steps.

    """
    file = open(filename)
    lights = []
    for line in file:
        line = line.strip().split()
        if len(line) > 0:
            lights.append([1 if l == '#' else 0 for l in line[0]])
    file.close()

    lights = np.array(lights)
    full_row, full_column = lights.shape
    for row in [0, full_row-1]:
        for column in [0, full_column-1]:
            lights[row, column] = 1

    for step in range(steps):
        new_lights = lights.copy()
        for row in range(full_row):
            for column in range(full_column):
                if row in [0, full_row-1] and column in [0, full_column-1]:
                    continue
                surroundings = [lights[n, m] for n in range(row-1, row+2) \
                                for m in range(column-1, column+2) if not (n == row and m == column) \
                                and n >= 0 and n < full_row and m >= 0 and m < full_column]
                if lights[row, column]:
                    if sum(surroundings) not in [2, 3]:
                        new_lights[row, column] = 0
                else:
                    if sum(surroundings) == 3:
                        new_lights[row, column] = 1
        lights = new_lights.copy()
        if animate:
            plt.imshow(lights,cmap='gray')
            plt.text(99-(9*len(str(step+1))), 10, str(step+1), {'color': 'r', 'fontsize': 25, 'fontweight': 'bold'})
            plt.show()

    num_on = lights.sum()

    return num_on
