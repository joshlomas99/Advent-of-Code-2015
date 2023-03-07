def get_input(input_file: str='Inputs/Day23_Inputs.txt') -> list:
    """
    Parse an input file to extract the list of instructions making up a program which edits the
    values of two registers.

    Parameters
    ----------
    input_file : str, optional
        Input file containing the program.
        The default is 'Inputs/Day23_Inputs.txt'.

    Returns
    -------
    program : list(list(str))
        The extracted list of instructions.

    """
    # Parse input file
    with open(input_file) as f:
        program = [line.strip().split() for line in f.readlines()]

    return program

# List of two register names
ALL_REG = ['a', 'b']

def run_instruction(register: list, i: int, program: list) -> tuple:
    """
    Run an instruction on a given line of a program to change the value of a given register, or to
    jump to a different line within the program, depending on certain criteria.

    Instructions
    ------------
    hlf
        Divides current register by 2.
    tpl
        Multiplies current register by 3.
    inc
        Increments current register by 1.
    jmp
        Increments line number i by a given amount.
    jie
        Increments line number i by a given amount if the current register is even.
    jio
        Increments line number i by a given amount if the current register is 1.

    Parameters
    ----------
    register : list(int)
        The list of different available registers to edit.
    i : int
        The current line number within the program being executed.
    program : list(list(str))
        The program being executed.

    Returns
    -------
    register : list(int)
        The registers after the instruction is run.
    i : int
        The current line number within the program after the instruction is run.

    """
    # Find the instruction on the current line of the program.
    instruction = program[i]
    # Find the reigster involved in this instruction
    curr_reg = instruction[1].strip(',')

    # hlf: divides current register by 2
    if instruction[0] == 'hlf':
        register[ALL_REG.index(curr_reg)] /= 2
    # tpl: multiplies current register by 3
    elif instruction[0] == 'tpl':
        register[ALL_REG.index(curr_reg)] *= 3
    # inc: increments current register by 1
    elif instruction[0] == 'inc':
        register[ALL_REG.index(curr_reg)] += 1
    # jmp: increments line number i by a given amount
    elif instruction[0] == 'jmp':
        return register, i + int(instruction[1])
    # jie: increments line number i by a given amount if the current register is even
    elif instruction[0] == 'jie':
        if register[ALL_REG.index(curr_reg)]%2 == 0:
            return register, i + int(instruction[2])
    # jio: increments line number i by a given amount if the current register is 1
    elif instruction[0] == 'jio':
        if register[ALL_REG.index(curr_reg)] == 1:
            return register, i + int(instruction[2])

    # If instruction didn't directly alter line number, increment it by 1
    return register, i + 1

def Day23_Part1(input_file='Inputs/Day23_Inputs.txt'):
    """
    Find the value of register b after execution of a program containing a series of instructions,
    given in an input file, which changes the values of a pair a registers [a, b], which both
    start at 0.

    Instructions
    ------------
    hlf
        Divides current register by 2.
    tpl
        Multiplies current register by 3.
    inc
        Increments current register by 1.
    jmp
        Increments line number i by a given amount.
    jie
        Increments line number i by a given amount if the current register is even.
    jio
        Increments line number i by a given amount if the current register is 1.

    Parameters
    ----------
    input_file : str, optional
        Input file containing the program to be executed.
        The default is 'Inputs/Day23_Inputs.txt'.

    Returns
    -------
    b : int
        The value of register b after the program is executed.

    """
    # Parse program input file
    program = get_input(input_file)

    # Set initial registers and line number
    register, i = [0, 0], 0

    # Execute the program
    while i < len(program):
        # Registers and line number can be altered by each instruction
        register, i = run_instruction(register, i, program)

    # Second value is register b
    b = register[1]

    return b

def Day23_Part2(input_file='Inputs/Day23_Inputs.txt'):
    """
    Find the value of register b after execution of a program containing a series of instructions,
    given in an input file, which changes the values of a pair a registers [a, b], which start at
    [1, 0] respectively.

    Instructions
    ------------
    hlf
        Divides current register by 2.
    tpl
        Multiplies current register by 3.
    inc
        Increments current register by 1.
    jmp
        Increments line number i by a given amount.
    jie
        Increments line number i by a given amount if the current register is even.
    jio
        Increments line number i by a given amount if the current register is 1.

    Parameters
    ----------
    input_file : str, optional
        Input file containing the program to be executed.
        The default is 'Inputs/Day23_Inputs.txt'.

    Returns
    -------
    b : int
        The value of register b after the program is executed.

    """
    # Parse program input file
    program = get_input(input_file)

    # Set initial registers and line number
    register, i = [1, 0], 0

    # Execute the program
    while i < len(program):
        # Registers and line number can be altered by each instruction
        register, i = run_instruction(register, i, program)

    # Second value is register b
    b = register[1]

    return b
