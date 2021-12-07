import shlex
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
    dimensions_list = []
    for line in file:
        line = line.strip()
        line = shlex.split(line)
        if len(line) > 0:
            dimensions_list.append(line)
    file.close()
    
    formatted_dimensions = []
    for dim_set in dimensions_list:
        dimensions, i = [], 0
        while i < len(dim_set[0]):
            curr_dim = ''
            while i < len(dim_set[0]) and dim_set[0][i] != 'x':
                curr_dim += dim_set[0][i]
                i += 1
            dimensions.append(int(curr_dim))
            i += 1
        formatted_dimensions.append(dimensions)

    total_area = 0
    for dims in formatted_dimensions:
        smallest_side = False
        for indices in [[0, 1], [0, 2], [1, 2]]:
            total_area += 2*dims[indices[0]]*dims[indices[1]]
            if not smallest_side or dims[indices[0]]*dims[indices[1]] < smallest_side:
                smallest_side = dims[indices[0]]*dims[indices[1]]
        total_area += smallest_side
            
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
    dimensions_list = []
    for line in file:
        line = line.strip()
        line = shlex.split(line)
        if len(line) > 0:
            dimensions_list.append(line)
    file.close()
    
    formatted_dimensions = []
    for dim_set in dimensions_list:
        dimensions, i = [], 0
        while i < len(dim_set[0]):
            curr_dim = ''
            while i < len(dim_set[0]) and dim_set[0][i] != 'x':
                curr_dim += dim_set[0][i]
                i += 1
            dimensions.append(int(curr_dim))
            i += 1
        formatted_dimensions.append(dimensions)

    total_length = 0
    for dims in formatted_dimensions:
        smallest_face = False
        for indices in [[0, 1], [0, 2], [1, 2]]:
            if not smallest_face or 2 * (dims[indices[0]] + dims[indices[1]]) < smallest_face:
                smallest_face = 2 * (dims[indices[0]] + dims[indices[1]])
        total_length += smallest_face
        total_length += np.product(dims)
            
    return total_length
