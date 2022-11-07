def Day7_Part1(filename='Inputs/Day7_Inputs.txt'):
    """
    Evaluates the value of the 16-bit signal in every wire of a circuit in which the wires are
    connected according to a series of logic gates specified in an input file.
    
    Parameters
    ----------
    filename : str, optional
        Input file containing the connections.
        The default is 'Inputs/Day7_Inputs.txt'.

    Returns
    -------
    a_signal : int
        The value of the signal in wire 'a' once the circuit is fully evaluated.
    
    """
    file = open(filename)
    wires = {}
    for line in file:
        line = line.strip().split(' -> ')
        if len(line) > 0:
            if line[1] in wires:
                raise Exception('Overlapping signals')
            signal = line[0].replace('AND', '&').replace('OR', '|').replace('NOT', '~').split()
            for i in range(len(signal)):
                if type(signal[i]) == str and signal[i].islower():
                    signal[i] = 'wires["' + signal[i] + '"]'
            wires[line[1]] = ' '.join(signal).replace('LSHIFT', '<<').replace('RSHIFT', '>>')
    file.close()

    changed = True
    while changed:
        changed = False
        for wire in wires:
            if type(wires[wire]) == int:
                continue
            try:
                wires[wire] = eval(wires[wire])%(2**16)
                changed = True
            except(TypeError):
                pass

    a_signal = wires['a']

    return a_signal

def Day7_Part2(filename='Inputs/Day7_Inputs.txt'):
    """
    Evaluates the value of the 16-bit signal in every wire of a circuit in which the wires are
    connected according to a series of logic gates specified in an input file, but with the signal
    of wire 'b' overrided to the final value of wire 'a' from Part 1 (46,065).
    
    Parameters
    ----------
    filename : str, optional
        Input file containing the connections.
        The default is 'Inputs/Day7_Inputs.txt'.

    Returns
    -------
    a_signal : int
        The value of the signal in wire 'a' once the circuit is fully evaluated.
    
    """
    file = open(filename)
    wires = {}
    for line in file:
        line = line.strip().split(' -> ')
        if len(line) > 0:
            if line[1] in wires:
                raise Exception('Overlapping signals')
            signal = line[0].replace('AND', '&').replace('OR', '|').replace('NOT', '~').split()
            for i in range(len(signal)):
                if type(signal[i]) == str and signal[i].islower():
                    signal[i] = 'wires["' + signal[i] + '"]'
            wires[line[1]] = ' '.join(signal).replace('LSHIFT', '<<').replace('RSHIFT', '>>')
    file.close()

    wires['b'] = 46065

    changed = True
    while changed:
        changed = False
        for wire in wires:
            if type(wires[wire]) == int:
                continue
            try:
                wires[wire] = eval(wires[wire])%(2**16)
                changed = True
            except(TypeError):
                pass

    a_signal = wires['a']

    return a_signal
