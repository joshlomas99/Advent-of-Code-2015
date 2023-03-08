def get_input(input_file: str='Inputs/Day24_Inputs.txt') -> set:
    """
    Parse an input file containing the weights of a set of packages.

    Parameters
    ----------
    input_file : str, optional
        Input file containing the package weights.
        The default is 'Inputs/Day24_Inputs.txt'.

    Returns
    -------
    packages : set(int)
        Set of the different package weights.

    """
    # Parse input file
    with open(input_file) as f:
        # Make a set of the integer weights
        packages = {int(line.strip()) for line in f.readlines()}

    return packages
    
from itertools import combinations
from functools import reduce
import operator

def Day24_Part1(input_file: str='Inputs/Day24_Inputs.txt') -> int:
    """
    Finds the quantum entanglement of the first group of packages, when a set of packages, whose
    weights are given in an input file, are arranged into three groups of equal total weight in
    the ideal configuration, such that the first group contains as few packages as possible, and
    given that has the smallest quantum entanglement possible. The quantum entanglement of a group
    of packages is the product of their weights.

    Parameters
    ----------
    input_file : str, optional
        Input file containing the package weights.
        The default is 'Inputs/Day24_Inputs.txt'.

    Returns
    -------
    quantum_entanglement : int
        The quantum entanglement of the first group of packages in the ideal configuration.

    """
    # Parse input file to extract the package weights
    packages = get_input(input_file)

    # Starting with no candidates for group 1 composition, and a group 1 size of 1, and increasing
    # size until we find possible candidates, as we want to minimise group 1 size
    group_1, group_1_size = {}, 1
    # While no candidates have been found for the current group 1 size
    while not group_1:
        # Find every possible group of packages of the current tested size, such that the sum of
        # the weights is a third of the total weight
        group_1 = {group for group in combinations(packages, group_1_size) if sum(group) == sum(packages)/3}
        group_1_size += 1

    # Sort group 1 candidates by quantum entanglement (product of weights), to test more ideal
    # configurations first
    group_1 = sorted(group_1, key=lambda x: reduce(operator.mul, x))

    # For each group 1 candidate
    for g1 in group_1:
        # Find which packages are left to sort into groups 2 and 3
        left = packages.difference(set(g1))
        # If there are any arrangements of groups 2 and 3 such that group 2 has a sum of a third
        # of the total weight, group 3 must have the same so we have found a possible configuration
        # and the first possible configuration found here must be the ideal one
        if any(g2 for i in range(len(left)) for g2 in combinations(left, i) \
                if sum(g2) == sum(packages)/3):
            # Return the quantum entanglement
            quantum_entanglement = reduce(operator.mul, g1)
            return quantum_entanglement

    # Return None if no possible configurations exist
    return None

def Day24_Part2(input_file: str='Inputs/Day24_Inputs.txt') -> int:
    """
    Finds the quantum entanglement of the first group of packages, when a set of packages, whose
    weights are given in an input file, are arranged into four groups of equal total weight in
    the ideal configuration, such that the first group contains as few packages as possible, and
    given that has the smallest quantum entanglement possible. The quantum entanglement of a group
    of packages is the product of their weights.

    Parameters
    ----------
    input_file : str, optional
        Input file containing the package weights.
        The default is 'Inputs/Day24_Inputs.txt'.

    Returns
    -------
    quantum_entanglement : int
        The quantum entanglement of the first group of packages in the ideal configuration.

    """
    # Parse input file to extract package weights
    packages = get_input(input_file)
        
    # Starting with no candidates for group 1 composition, and a group 1 size of 1, and increasing
    # size until we find possible candidates, as we want to minimise group 1
    group_1, group_1_size = {}, 1
    # While no candidates have been found for the current group 1 size
    while not group_1:
        # Find every possible group of packages of the current tested size, such that the sum of
        # the weights is a quarter of the total weight
        group_1 = {group for group in combinations(packages, group_1_size) if sum(group) == sum(packages)/4}
        group_1_size += 1
    
    # Sort group 1 candidates by quantum entanglement (product of weights), to test more ideal
    # configurations first
    group_1 = sorted(group_1, key=lambda x: reduce(operator.mul, x))
    
    # For each group 1 candidate
    for g1 in group_1:
        # Find which packages are left to sort into groups 2, 3 and 4
        left = packages.difference(set(g1))
        # For all possible sizes of group 2, starting from 1 since smaller sizes are more likely
        for i in range(len(left)):
            # Find the possible configurations of group 2 with the current size
            for g2 in combinations(left, i):
                # If the sum of weights is not a quarter of the total weight, this is not a valid
                # candidate, so move on
                if sum(g2) != sum(packages)/4:
                    continue

                # Else group 2 is the correct size, so if there are also any arrangements of
                # groups 3 and 4 such that group 3 has a sum of a quarter of the total weight,
                # group 4 must have the same so we have found a possible configuration, and the
                # first possible configuration found here must be the ideal one
                if any(g3 for j in range(len(left) - i) \
                        for g3 in combinations(left.difference(set(g2)), j) \
                        if sum(g3) == sum(packages)/4):
                    # Return the quantum entanglement
                    quantum_entanglement = reduce(operator.mul, g1)
                    return quantum_entanglement

    # Return None if no possible configurations exist
    return None
