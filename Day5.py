import shlex

def Day5_Part1(filename='Inputs/Day5_Inputs.txt', printout=False):
    """
    Calculates the number of nice words in a given input file. A nice string is one which:
        - Contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
        - AND contains at least one letter that appears twice in a row, like xx, abcdde (dd),
        or aabbccdd (aa, bb, cc, or dd).
        - AND does not contain the strings ab, cd, pq, or xy, even if they are part of one
        of the other requirements.

    Parameters
    ----------
    filename : str, optional
        Input file containing the strings to be judged.
        The default is 'Inputs/Day5_Inputs.txt'.
    printout : bool, optional
        Whether or not to print information about each string.
        The default is False.

    Returns
    -------
    nice : int
        The number of nice strings in the input file.

    """
    file = open(filename)
    strings = []
    for line in file:
        line = line.strip()
        line = shlex.split(line)
        if len(line) > 0:
            strings.append(line[0])
    file.close()
    
    nice = 0
    illegal_chars = ['ab', 'cd', 'pq', 'xy']
    vowels = ['a', 'e', 'i', 'o', 'u']
    for string in strings:
        if any(string.count(illegal) > 0 for illegal in illegal_chars):
            if printout:
                char_found = illegal_chars[list(string.count(illegal) > 0 for illegal in illegal_chars).index(True)]
                print(f'{string} is naughty because it contains the string {char_found}!')
            
        elif sum(string.count(vowel) for vowel in vowels) < 3:
            if printout:
                num_vowels = sum(string.count(vowel) for vowel in vowels)
                num_vowels_word = ['no', 'one', 'two'][num_vowels]
                print(f'{string} is naughty because it contains ' + 'only '*(num_vowels > 0) + f'{num_vowels_word} vowel' + 's'*(num_vowels != 1) + '!')
            
        elif not any(list(string[i] == string[i+1] for i in range(len(string)-1))):
            if printout:
                print(f'{string} is naughty because it has no double letter!')
            
        else:
            nice += 1
            if printout:
                print(f'{string} is nice!')
    
    return nice

def Day5_Part2(filename='Inputs/Day5_Inputs.txt', printout=False):
    """
    Calculates the number of nice words in a given input file, but with different rules.
    Now a nice string is one which:
        - Contains a pair of any two letters that appears at least twice in the string
        without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but
        it overlaps).
        - AND contains at least one letter which repeats with exactly one letter between
        them, like xyx, abcdefeghi (efe), or even aaa.

    Parameters
    ----------
    filename : str, optional
        Input file containing the strings to be judged.
        The default is 'Inputs/Day5_Inputs.txt'.
    printout : bool, optional
        Whether or not to print information about each string.
        The default is False.

    Returns
    -------
    nice : int
        The number of nice strings in the input file.

    """
    file = open(filename)
    strings = []
    for line in file:
        line = line.strip()
        line = shlex.split(line)
        if len(line) > 0:
            strings.append(line[0])
    file.close()
    
    nice = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for string in strings:
        if not any(string.count(lettera + letterb) >= 2 for lettera in alphabet for letterb in alphabet):
            if printout:
                print(f'{string} is naughty because it has no pair that appears twice!')
            
        elif not any(list(string[i] == string[i+2] for i in range(len(string)-2))):
            if printout:
                print(f'{string} is naughty because it has no repeat with a single letter between them!')
            
        else:
            nice += 1
            if printout:
                print(f'{string} is nice!')
    
    return nice