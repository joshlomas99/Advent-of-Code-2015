def Day19_Part1(filename='Inputs/Day19_Inputs.txt'):
    """
    Calculates the number of distinct molecules which can be created after one step of replacement
    from a starting molecule given in an input file, where the available replacements are also
    given in the input file.

    Parameters
    ----------
    filename : str, optional
        Input file giving starting molecule and available replacements.
        The default is 'Inputs/Day19_Inputs.txt'.

    Returns
    -------
    num_combinations : int
        The number of distinct molecules which can be created.

    """
    # Parse input file
    file = open(filename)
    calibration = {}
    for line in file:
        line = line.strip().split()
        if len(line) > 0:
            if len(line) == 3:
                # Fill dictionary with available replacements
                if line[0] in calibration:
                    calibration[line[0]].append(line[2])
                else:
                    calibration[line[0]] = [line[2]]
            else:
                # Starting molecule
                medicine = line[0]
    file.close()

    # Initialise set of distinct possible molecules
    molecules = set()

    # Loop through substrings to be replaced
    for mol in calibration:
        # Loop through substrings to replace mol with
        for rep in calibration[mol]:
            # Find first occurance of substring to be replaced
            ind = medicine.find(mol)
            while ind >= 0: # While it hasn't reached the end of the starting molecule
                # Replace the next occurance of the substring to obtain a new molecule
                # and add it to the set
                molecules.add(medicine[:ind] + medicine[ind:].replace(mol, rep, 1))
                # Find next occurance of substring to be replaced
                ind = medicine.find(mol, ind+1)

    # Number of distinct values in the set
    num_combinations = len(molecules)

    return num_combinations

def Day19_Part2(filename='Inputs/Day19_Inputs.txt', total=150):
    """
    Calculates the fewest number of steps of replacement required to go from a starting molecule
    "e" to a final molecules given in an input file, where the available replacements are also
    given in the input file.

    Parameters
    ----------
    filename : str, optional
        Input file giving final molecule and available replacements.
        The default is 'Inputs/Day19_Inputs.txt'.

    Returns
    -------
    min_steps : int
        The minimum number of steps required to obtain the final molecule starting from "e".

    """
    file = open(filename)
    calibration = {}
    for line in file:
        line = line.strip().split()
        if len(line) > 0:
            if len(line) == 3:
                if line[0] in calibration:
                    calibration[line[0]].append(line[2])
                else:
                    calibration[line[0]] = [line[2]]
            else:
                medicine = line[0]
    file.close()

    # Number of atoms in molecule
    total_elements = len([c for c in medicine if c.isupper()])
    # Number of key elements in molecule
    num_Ar, num_Rn, num_Y = medicine.count('Ar'), medicine.count('Rn'), medicine.count('Y')
    # Analytical solution
    min_steps = total_elements - 1 - num_Ar - num_Rn - (2*num_Y)

    return min_steps
