def increment(string):
    """
    Increments a given string like counting with numbers: xx, xy, xz, ya, yb, and so on.
    Increase the rightmost letter one step; if it was z, it wraps around to a, and repeat with the
    next letter to the left until one doesn't wrap around.

    Parameters
    ----------
    string : str
        The string to increment.

    Returns
    -------
    string : str
        The incremented string.

    """
    i = len(string) - 1
    while i >= 0:
        new_char = chr(((ord(string[i])+1 - 97)%26)+97)
        chars = [c for c in string]
        chars[i] = new_char
        string = ''.join(chars)
        if string[i] == 'a':
            i -= 1
        else:
            return string
    return string

def passwordCheck(password):
    """
    Checks whether a password meets the following requirements:
        Passwords must include one increasing straight of at least three letters, like abc, bcd, cde,
        and so on, up to xyz. They cannot skip letters; abd doesn't count.

        Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other
        characters and are therefore confusing.

        Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb,
        or zz.
    
    Parameters
    ----------
    password : str
        The password to check.

    Returns
    -------
    valid : bool
        Whether the password passes the requirements or not.

    """
    if sum([password.count(c) for c in ['i', 'l', 'o']]) > 0:
        # print('Contains illegal letter')
        return False
    consec_char, num_consec, consec_set = None, 0, False
    repeat_char, repeat = None, 0
    for char in password[1:]:
        if repeat < 2:
            if not repeat_char:
                repeat_char = 1*char
            elif char == repeat_char:
                repeat += 1
                repeat_char = None
            else:
                repeat_char = 1*char
        if not consec_set:
            if not consec_char:
                consec_char = 1*char
                num_consec = 1
            elif ord(char) == ord(consec_char) + 1:
                num_consec += 1
                if num_consec >= 3:
                    consec_set = True
                else:
                    consec_char = 1*char
            else:
                consec_char = 1*char
                num_consec = 1

    if not consec_set:
        # print('No consecutive set')
        return False
    if repeat < 2:
        # print('<2 repeating pairs')
        return False

    return True

def Day11_Part1(filename='Inputs/Day11_Inputs.txt'):
    """
    Finds the next valid password in the sequence given by incrementing a starting password given
    in an input file like a number (xx, xy, xz, ya, yb, and so on) where the password requirements
    are given below.

    Password Requirements
    ---------------------
    Passwords must include one increasing straight of at least three letters, like abc, bcd, cde,
    and so on, up to xyz. They cannot skip letters; abd doesn't count.

    Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other
    characters and are therefore confusing.

    Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb,
    or zz.

    Parameters
    ----------
    filename : str, optional
        Input file containing the original password.
        The default is 'Inputs/Day11_Inputs.txt'.

    Returns
    -------
    password : str
        The next valid password after repeatedly incrementing the original one.

    """
    file = open(filename)
    password = None
    for line in file:
        line = line.strip().split()
        if len(line) > 0:
            password = line[0]
    file.close()

    while not passwordCheck(password):
        password = increment(password)
        if sum([password.count(c) for c in ['i', 'l', 'o']]) > 0:
            index = min([password.find(c)%len(password) for c in ['i', 'l', 'o']])
            parts = password.partition(password[index])
            password = increment(parts[0] + parts[1]) + 'a'*len(parts[2])

    return password

def Day11_Part2(password=increment('hepxxyzz')):
    """
    Finds the next valid password in the sequence given by incrementing a given starting password
    like a number (xx, xy, xz, ya, yb, and so on) where the password requirements are given below.

    Password Requirements
    ---------------------
    Passwords must include one increasing straight of at least three letters, like abc, bcd, cde,
    and so on, up to xyz. They cannot skip letters; abd doesn't count.

    Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other
    characters and are therefore confusing.

    Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb,
    or zz.

    Parameters
    ----------
    password : str
        The starting password.

    Returns
    -------
    password : str
        The next valid password after repeatedly incrementing the original one.

    """
    start = password[:4]
    while not passwordCheck(password):
        password = increment(password)
        if sum([password.count(c) for c in ['i', 'l', 'o']]) > 0:
            index = min([password.find(c)%len(password) for c in ['i', 'l', 'o']])
            parts = password.partition(password[index])
            password = increment(parts[0] + parts[1]) + 'a'*len(parts[2])
        if password[:4] != start:
            start = password[:4]
            print(start)

    return password