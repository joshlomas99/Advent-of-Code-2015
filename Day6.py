import numpy as np

class Instruction:
    """
    Class describing an instruction for controlling lights.
    """
    def __init__(self, type_, coords):
        """
        Initialise the class with two parameters.

        Parameters
        ----------
        type_ : str
            The instruction to perform, options are 'on', 'off' and 'toggle'.

        coords : list of lists of ints
            The two sets of coordinates bounding the set of lights to be affected.
            e.g. [[0, 0], [1, 1]] affects lights at [0, 0], [0, 1], [1, 0], [1, 1].                                                
            
        Returns
        -------
        None.

        """
        self.type = type_
        self.coords = coords

    def __repr__(self):
        """
        Return the representation of an Instruction object.

        Returns
        -------
        str
            Representation.

        """
        return '{}({}, {})'.format(self.__class__.__name__, self.type, self.coords)

def Day6_Part1(filename='Inputs/Day6_Inputs.txt'):
    """
    Returns the number of lights out of an 1000 x 1000 grid which are lit after following a set of
    instructions given in an input file, with all lights starting as off.

    e.g. "turn on 0,0 through 999,999" would turn on (or leave on) every light
    "toggle 0,0 through 999,0" would toggle the first line of 1000 lights, turning off the ones
    that were on, and turning on the ones that were off
    "turn off 499,499 through 500,500" would turn off (or leave off) the middle four lights

    Parameters
    ----------
    filename : str, optional
        Input file containing the instructions.
        The default is 'Inputs/Day6_Inputs.txt'.

    Returns
    -------
    lit_number : int
        The number of lights which are lit.

    """
    file = open(filename)
    instructions = []
    for line in file:
        line = line.strip().split()
        if len(line) > 0:
            if line[0] == 'toggle':
                type_ = line[0]
            else:
                type_ = line[1]
            coords_from = tuple([int(i) for i in line[-3].split(',')])
            coords_to = tuple([int(i) for i in line[-1].split(',')])
            instructions.append(Instruction(type_, [coords_from, coords_to]))
    file.close()

    lights = np.zeros((1000, 1000))
    for instruction in instructions:
        if instruction.type == 'on':
            lights[instruction.coords[0][0]:instruction.coords[1][0]+1,
                   instruction.coords[0][1]:instruction.coords[1][1]+1] = 1
        elif instruction.type == 'off':
            lights[instruction.coords[0][0]:instruction.coords[1][0]+1,
                   instruction.coords[0][1]:instruction.coords[1][1]+1] = 0
        elif instruction.type == 'toggle':
            lights[instruction.coords[0][0]:instruction.coords[1][0]+1,
                   instruction.coords[0][1]:instruction.coords[1][1]+1] += 1
            lights[instruction.coords[0][0]:instruction.coords[1][0]+1,
                   instruction.coords[0][1]:instruction.coords[1][1]+1] %= 2
        else:
            raise Exception(f'Unrecognised instruction: {instruction.type}')

    lit_number = int(np.sum(lights))

    return lit_number

def Day6_Part2(filename='Inputs/Day6_Inputs.txt'):
    """
    Returns the total brightness of all lights out of an 1000 x 1000 grid which are lit after
    following a set of instructions given in an input file, with all lights starting as off.

    The phrase "turn on" now means that you should increase the brightness of those lights by 1.
    The phrase "turn off" now means that you should decrease the brightness of those lights by 1,
    to a minimum of zero.
    The phrase "toggle" now means that you should increase the brightness of those lights by 2.

    Parameters
    ----------
    filename : str, optional
        Input file containing the instructions.
        The default is 'Inputs/Day6_Inputs.txt'.

    Returns
    -------
    total_brightness : int
        The total brightness of all the lights.

    """
    file = open(filename)
    instructions = []
    for line in file:
        line = line.strip().split()
        if len(line) > 0:
            if line[0] == 'toggle':
                type_ = line[0]
            else:
                type_ = line[1]
            coords_from = tuple([int(i) for i in line[-3].split(',')])
            coords_to = tuple([int(i) for i in line[-1].split(',')])
            instructions.append(Instruction(type_, [coords_from, coords_to]))
    file.close()

    lights = np.zeros((1000, 1000))
    for instruction in instructions:
        if instruction.type == 'on':
            lights[instruction.coords[0][0]:instruction.coords[1][0]+1,
                   instruction.coords[0][1]:instruction.coords[1][1]+1] += 1
        elif instruction.type == 'off':
            lights[instruction.coords[0][0]:instruction.coords[1][0]+1,
                   instruction.coords[0][1]:instruction.coords[1][1]+1] -= 1
            lights[lights < 0] = 0
        elif instruction.type == 'toggle':
            lights[instruction.coords[0][0]:instruction.coords[1][0]+1,
                   instruction.coords[0][1]:instruction.coords[1][1]+1] += 2
        else:
            raise Exception(f'Unrecognised instruction: {instruction.type}')

    total_brightness = int(np.sum(lights))

    return total_brightness
