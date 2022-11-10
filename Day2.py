import numpy as np

def Day2_Part1(filename='Inputs/Day2_Inputs.txt'):
    """
    Calculate the total area of wrapping paper required to wrap all of the presents, whose
    dimensions are given as a list in an input file. The wrapping paper required for each
    present is the surface area plus the area of the smallest side.

    Parameters
    ----------
    filename : str, optional
        Input file giving the dimensions of every present.
        The default is 'Inputs/Day2_Inputs.txt'.

    Returns
    -------
    total_area : int
        Total area of wrapping paper required.

    """
    file = open(filename)
    dimensions = []
    for line in file:
        line = line.strip().split()
        if len(line) > 0:
            dimensions.append([int(i) for i in line[0].split('x')])
    file.close()

    d = np.array(dimensions)
    faces = np.array([d[:, indices[0]]*d[:, indices[1]] for indices in [[0, 1], [0, 2], [1, 2]]]).T
    total_area  = np.sum(2*np.sum(faces, axis=1) + np.min(faces, axis=1))

    return total_area

def Day2_Part2(filename='Inputs/Day2_Inputs.txt'):
    """
    Calculate the total length of ribbon required to wrap all of the presents, whose
    dimensions are given as a list in an input file. The length of ribbon required for
    each present is the perimeter of the smallest side plus the volume of the present.

    Parameters
    ----------
    filename : str, optional
        Input file giving the dimensions of every present.
        The default is 'Inputs/Day2_Inputs.txt'.

    Returns
    -------
    total_length : int
        Total length of ribbon required.

    """
    file = open(filename)
    dimensions = []
    for line in file:
        line = line.strip().split()
        if len(line) > 0:
            dimensions.append([int(i) for i in line[0].split('x')])
    file.close()

    d = np.array(dimensions)
    perimeters = np.array([2*(d[:, indices[0]] + d[:, indices[1]]) for indices in [[0, 1], [0, 2], [1, 2]]]).T
    total_length  = np.sum(np.min(perimeters, axis=1) + np.product(d, axis=1))
            
    return total_length
