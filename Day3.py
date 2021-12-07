import shlex

class Coordinates:
    """
    Class to define a pair of coordinates (x, y)
    """
    def __init__(self, pos):
        """
        Initialise the class with one parameter.

        Parameters
        ----------
        pos : list of int
            Coordinates in the form [x, y].
            
        Returns
        -------
        None.

        """
        self.x = pos[0]
        self.y = pos[1]
    
    def __repr__(self):
        """
        Return the representation of a Coordinates object.

        Returns
        -------
        str
            Representation.

        """
        return f'{self.__class__.__name__}({self.x}, {self.y})'
    
    def __hash__(self):
        """
        Override the hash function for a Coordinates object.

        Returns
        -------
        int
            The hash of the Coordinates.

        """
        return hash((self.x, self.y))

    def __eq__(self, other):
        """
        Overrides the == operator for a Coordinates object.

        Parameters
        ----------
        other : Coordinates
            The Coordinates object to which we are comparing.

        Returns
        -------
        bool
            Whether the two Coordinates are equivalent or not.

        """
        return (self.x, self.y) == (other.x, other.y)

    def __ne__(self, other):
        """
        Overrides the != operator for a Coordinates object.

        Parameters
        ----------
        other : Coordinates
            The Coordinates object to which we are comparing.

        Returns
        -------
        bool
            Whether the two Coordinates are different or not.

        """
        return not(self == other)

def Day3_Part1(filename='Inputs/Day3_Inputs.txt'):
    """
    Returns the number of houses in an infinite 2D map of houses which get at least one
    present delivered, when Santa starts at (0, 0) and moves according to a series of
    instructions, given in an input file, delivering a present at every stop.

    Parameters
    ----------
    filename : str, optional
        Input file giving the directions.
        The default is 'Inputs/Day3_Inputs.txt'.

    Raises
    ------
    Exception
        Unknown direction encountered.

    Returns
    -------
    num_houses : int
        The number of houses which recieve at least one present.

    """
    file = open(filename)
    directions = []
    for line in file:
        line = line.strip()
        line = shlex.split(line)
        if len(line) > 0:
            directions.append(line)
    file.close()
    
    pos = [0, 0]
    map_ = {}
    map_[Coordinates(pos)] = 1
    for direction in directions[0][0]:
        if direction == '^':
            pos[1] += 1
        elif direction == '>':
            pos[0] += 1
        elif direction == 'v':
            pos[1] -= 1
        elif direction == '<':
            pos[0] -= 1
        else:
            raise Exception('Unknown direction!')
        try:
            map_[Coordinates(pos)] += 1
        except:
            map_[Coordinates(pos)] = 1
    
    num_houses = len(map_)
    return num_houses

def Day3_Part2(filename='Inputs/Day3_Inputs.txt'):
    """
    Returns the number of houses in an infinite 2D map of houses which get at least one
    present delivered, when Santa and Robot Santa start at (0, 0) and take turns moving
    according to a series of instructions, given in an input file, delivering a present
    at every stop.

    Parameters
    ----------
    filename : str, optional
        Input file giving the directions.
        The default is 'Inputs/Day3_Inputs.txt'.

    Raises
    ------
    Exception
        Unknown direction encountered.

    Returns
    -------
    num_houses : int
        The number of houses which recieve at least one present.

    """
    file = open(filename)
    directions = []
    for line in file:
        line = line.strip()
        line = shlex.split(line)
        if len(line) > 0:
            directions.append(line)
    file.close()
 
    santa_pos = [0, 0]
    robot_pos = [0, 0]
    map_ = {}
    map_[Coordinates([0, 0])] = 2
    for n, direction in enumerate(directions[0][0]):
        if direction == '^':
            if n%2 == 0:
                santa_pos[1] += 1
            else:
                robot_pos[1] += 1
        elif direction == '>':
            if n%2 == 0:
                santa_pos[0] += 1
            else:
                robot_pos[0] += 1
        elif direction == 'v':
            if n%2 == 0:
                santa_pos[1] -= 1
            else:
                robot_pos[1] -= 1
        elif direction == '<':
            if n%2 == 0:
                santa_pos[0] -= 1
            else:
                robot_pos[0] -= 1
        else:
            raise Exception('Unknown direction!')
        try:
            if n%2 == 0:
                map_[Coordinates(santa_pos)] = 1
            else:
                map_[Coordinates(robot_pos)] = 1
        except:
            if n%2 == 0:
                map_[Coordinates(santa_pos)] += 1
            else:
                map_[Coordinates(robot_pos)] += 1
    
    num_houses = len(map_)
    return num_houses