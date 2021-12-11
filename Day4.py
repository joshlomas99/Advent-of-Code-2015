import shlex
import numpy as np
from hashlib import md5

class unsigned32:
    """
    Class defining an unsigned 32-bit binary number.
    """
    
    def __init__(self, binary):
        """
        Initialise the class with one parameter, a binary string.

        Parameters
        ----------
        binary : str
            A number in binary in the form e.g. '10100010' (162 in decimal).

        """
        self.bin = '0'*(32 - len(binary)) + binary
    
    def binary(self, endiness='big'):
        """
        Returns the binary form of the 32-bit number using the specified endiness.

        Parameters
        ----------
        endiness : str, optional
            The endiness with which to print the binary number.
            Options are 'big' and 'little'. The default is 'big'.

        Returns
        -------
        str
            The binary form of the 32-bit number with the specified endiness.

        """
        if endiness == 'big':
            return self.bin
        elif endiness == 'little':
            out = ''
            for index_8 in range(int(len(self.bin)/8)):
                out = self.bin[int(8*index_8):int(8*(index_8+1))] + out
            return out
    
    def hexa(self, endiness='big'):
        """
        Returns the hexadecimal form of the 32-bit number using the specified endiness.

        Parameters
        ----------
        endiness : str, optional
            The endiness with which to print the hexadecimal number.
            Options are 'big' and 'little'. The default is 'big'.

        Returns
        -------
        str
            The hexadecimal form of the 32-bit number with the specified endiness.

        """
        short_hex = hex(int(self.bin, base=2))[2:]
        long_hex = '0'*(8 - len(short_hex)) + short_hex
        if endiness == 'big':
            return long_hex
        elif endiness == 'little':
            out = ''
            for index_2 in range(int(len(long_hex)/2)):
                out = long_hex[int(2*index_2):int(2*(index_2+1))] + out
            return out
            
    
    def dec(self):
        """
        Returns the decimal form of the 32-bit number.

        Returns
        -------
        int
            The decimal form of the 32-bit number.

        """
        return int(self.bin, base=2)
        
    def __repr__(self):
        """
        Return the representation of the unsigned 32-bit integer.
        """
        #return copy of RightSensor
        return "{0}({1})".format(self.__class__.__name__, self.bin)
    
    def __pos__(self):
        """
        Return a copy of the unsigned 32-bit integer.
        """
        return self.__class__(1*self.bin)

def flip_byte_order(number, base='bin'):
    """
    Flips the order of the bytes in an input number of a specified base such that the most
    significant byte swaps with the least signifcant, etc.

    Parameters
    ----------
    number : str
        String giving the number to be flipped.
    base : str, optional
        The base of the input number.
        Options are 'bin' (binary) or 'hex' (hexadecimal). The default is 'bin'.

    Returns
    -------
    out : str
        The input number in the specified base with the order of its bytes flipped.

    """
    out = ''
    if base == 'bin':
        for index_8 in range(int(len(number)/8)):
            out = number[int(8*index_8):int(8*(index_8+1))] + out
    elif base == 'hex':
        for index_2 in range(int(len(number)/2)):
            out = number[int(2*index_2):int(2*(index_2+1))] + out
    return out

def flip_bits_in_byte(number, base='bin'):
    """
    Flips the order of the the bits in every byte in an input number of a specified base
    such that the most significant bit in a byte swaps with the least signifcant bit in
    that byte, etc.

    Parameters
    ----------
    number : str
        String giving the number to be flipped.
    base : str, optional
        The base of the input number.
        Options are 'bin' (binary) or 'hex' (hexadecimal). The default is 'bin'.

    Returns
    -------
    out : str
        The input number in the specified base with the order of the bits in every byte
        flipped.

    """
    out = ''
    if base == 'bin':
        for index_8 in range(int(len(number)/8)):
            out += number[int(8*index_8):int(8*(index_8+1))][::-1]
    elif base == 'hex':
        for index_2 in range(int(len(number)/2)):
            out += number[int(2*index_2):int(2*(index_2+1))][::-1]
    return out

def flip_bits_and_bytes(number, base='bin'):
    """
    Flips the order of the bytes in an input number of a specified base such that the most
    significant byte swaps with the least signifcant, etc. Then flips the order of the the
    bits in every byte such that the most significant bit in a byte swaps with the least
    signifcant bit in that byte, etc.

    Parameters
    ----------
    number : TYPE
        DESCRIPTION.
    base : TYPE, optional
        DESCRIPTION. The default is 'bin'.

    Returns
    -------
    str
        The input number in the specified base with the order of its bytes flipped and the
        order of the bits in every byte flipped.

    """
    return flip_bits_in_byte(flip_byte_order(number, base), base)

def NOT(binary):
    """
    Applies a bitwise NOT operation to an unsigned 32-bit binary number, which returns
    0 if the input bit is 1 and vice versa.

    Parameters
    ----------
    binary : unsigned32
        Input unsigned 32-bit number.

    Returns
    -------
    unsigned32
        The unsigned 32-bit binary number with a bitwise NOT operation applied.

    """
    out = ''
    for i in range(len(binary.bin)):
        out += str(int(binary.bin[i] == '0'))
    
    return unsigned32(out)

def AND(binary1, binary2):
    """
    Applies a bitwise AND operation to a pair of unsigned 32-bit binary numbers, which
    returns 1 if both input bits are 1 and 0 otherwise.

    Parameters
    ----------
    binary : unsigned32
        Input unsigned 32-bit number.

    Returns
    -------
    unsigned32
        The unsigned 32-bit binary result of applying a bitwise AND operation to the
        pair of input numbers.

    """
    out = ''
    for i in range(len(binary1.bin)):
        out += str(int(binary1.bin[i])*int(binary2.bin[i]))
    
    return unsigned32(out)

def OR(binary1, binary2):
    """
    Applies a bitwise OR operation to a pair of unsigned 32-bit binary numbers, which
    returns 1 if either input bits are 1 and 0 otherwise.

    Parameters
    ----------
    binary : unsigned32
        Input unsigned 32-bit number.

    Returns
    -------
    unsigned32
        The unsigned 32-bit binary result of applying a bitwise OR operation to the
        pair of input numbers.

    """
    out = ''
    for i in range(len(binary1.bin)):
        out += str(int(int(binary1.bin[i]) + int(binary2.bin[i]) >= 1))
    
    return unsigned32(out)

def XOR(binary1, binary2):
    """
    Applies a bitwise XOR operation to a pair of unsigned 32-bit binary numbers, which
    returns 0 if both input bits are the same and 1 otherwise.

    Parameters
    ----------
    binary : unsigned32
        Input unsigned 32-bit number.

    Returns
    -------
    unsigned32
        The unsigned 32-bit binary result of applying a bitwise XOR operation to the
        pair of input numbers.

    """
    out = ''
    for i in range(len(binary1.bin)):
        out += str(int(binary1.bin[i] != binary2.bin[i]))
    
    return unsigned32(out)

def F_MD5(B, C, D):
    """
    The F function from the MD5 hashing algorithm.

    Parameters
    ----------
    B : unsigned32
        The current value of the unsigned 32-bit binary buffer B in the MD5 hashing
        algorithm.
    C : unsigned32
        The current value of the unsigned 32-bit binary buffer C in the MD5 hashing
        algorithm.
    D : unsigned32
        The current value of the unsigned 32-bit binary buffer D in the MD5 hashing
        algorithm.

    Returns
    -------
    unsigned32
        The unsigned 32-bit binary result of applying the F function to the current values
        of buffers B, C and D.

    """
    return OR(AND(B, C), AND(NOT(B), D))

def G_MD5(B, C, D):
    """
    The G function from the MD5 hashing algorithm.

    Parameters
    ----------
    B : unsigned32
        The current value of the unsigned 32-bit binary buffer B in the MD5 hashing
        algorithm.
    C : unsigned32
        The current value of the unsigned 32-bit binary buffer C in the MD5 hashing
        algorithm.
    D : unsigned32
        The current value of the unsigned 32-bit binary buffer D in the MD5 hashing
        algorithm.

    Returns
    -------
    unsigned32
        The unsigned 32-bit binary result of applying the G function to the current values
        of buffers B, C and D.

    """
    return OR(AND(B, D), AND(C, NOT(D)))

def H_MD5(B, C, D):
    """
    The H function from the MD5 hashing algorithm.

    Parameters
    ----------
    B : unsigned32
        The current value of the unsigned 32-bit binary buffer B in the MD5 hashing
        algorithm.
    C : unsigned32
        The current value of the unsigned 32-bit binary buffer C in the MD5 hashing
        algorithm.
    D : unsigned32
        The current value of the unsigned 32-bit binary buffer D in the MD5 hashing
        algorithm.

    Returns
    -------
    unsigned32
        The unsigned 32-bit binary result of applying the H function to the current values
        of buffers B, C and D.

    """
    return XOR(XOR(B, C), D)

def I_MD5(B, C, D):
    """
    The I function from the MD5 hashing algorithm.

    Parameters
    ----------
    B : unsigned32
        The current value of the unsigned 32-bit binary buffer B in the MD5 hashing
        algorithm.
    C : unsigned32
        The current value of the unsigned 32-bit binary buffer C in the MD5 hashing
        algorithm.
    D : unsigned32
        The current value of the unsigned 32-bit binary buffer D in the MD5 hashing
        algorithm.

    Returns
    -------
    unsigned32
        The unsigned 32-bit binary result of applying the I function to the current values
        of buffers B, C and D.

    """
    return XOR(C, OR(B, NOT(D)))

def add_modulo(binary_list):
    """
    Adds up a list of unsigned 32-bit binary numbers, modulus 2^32.

    Parameters
    ----------
    binary_list : list of unsigned32
        List of unsigned 32-bit binary numbers to be added.

    Returns
    -------
    binary_add : unsigned32
        unsigned 32-bit binary result of the modulus addition.

    """
    dec_list = []
    for binary in binary_list:
        dec_list.append(int(binary.bin, base=2))
    binary_add = unsigned32(bin(sum(dec_list)%(2**32))[2:])
    return binary_add
        
def MD5(string):
    """
    Applies the MD5 hashing algorithm to an input string and returns the result in
    hexadecimal format.

    Parameters
    ----------
    string : str
        Input string to be hashed.

    Returns
    -------
    MD5_hash_hex : str
        MD5 hash of input string in hexadecimal format.

    """
    # convert input string to 8-bit ascii format
    binary_string = ""
    for char in string:
        binary_char = bin(ord(char))[2:]
        binary_string += '0' * (8 - len(binary_char)) + binary_char
    
    # pad string
    binary_string += '1'
    binary_string += '0' * (512 - 64 - (len(binary_string)%512))
    binary_string = flip_bits_in_byte(binary_string)
    
    # append 64-bit binary string length to string
    binary_string_length = bin((8*len(string)) % 2**64)[2:]
    binary_length_64 = '0' * (64 - (len(binary_string_length)%(2**64))) + binary_string_length
    binary_string += flip_bits_and_bytes(binary_length_64)
        
    # initialisation buffers
    A = '67452301'
    B = 'efcdab89'
    C = '98badcfe'
    D = '10325476'
    
    # in 32-bit binary
    a = unsigned32(bin(int(A, base=16))[2:])
    b = unsigned32(bin(int(B, base=16))[2:])
    c = unsigned32(bin(int(C, base=16))[2:])
    d = unsigned32(bin(int(D, base=16))[2:])
    
    # functions
    F = lambda B, C, D : (B & C) | (~B & D)
    G = lambda B, C, D : (B & D) | (C & ~D)
    H = lambda B, C, D : (B ^ C) ^ D
    I = lambda B, C, D : C ^ (B | ~D)
    F_list = [F, G, H, I]
    
    # M_list indices
    round_1_indices = [i for i in range(16)]
    round_2_indices = [(5*i + 1) % 16 for i in range(16)]
    round_3_indices = [(3*i + 5) % 16 for i in range(16)]
    round_4_indices = [(7*i) % 16 for i in range(16)]
    index_list = round_1_indices + round_2_indices + round_3_indices + round_4_indices
    
    # k constants
    K_list = [unsigned32(bin(int(abs(np.sin(i + 1))*(2**32)))[2:]) for i in range(64)]
    
    # S shifts
    shift_lists = [[7, 12, 17, 22], [5, 9, 14, 20], [4, 11, 16, 23], [6, 10, 15, 21]]
    S_list = [shift_list[i%4] for shift_list in shift_lists for i in range(16)]

    # loop through 512-bit chunks of the string
    for binary_chunk in [binary_string[512*i:512*(i+1)] for i in range(len(binary_string)//512)]:
        
        # seperate 512-bit chunk into 16 32-bit chunks
        M_list = [unsigned32(flip_bits_and_bytes(unsigned32(binary_chunk[32*i:32*(i+1)]).bin)) for i in range(len(binary_chunk)//32)]
        
        # store original initialisation vectors
        a0, b0, c0, d0 = +a, +b, +c, +d
        
        # loop through 64 loops of the encryption in 4 16-part rounds
        for i in range(64):
            
            # apply corresponding function for current round
            f = F_list[i//16](int(b.bin, base=2), int(c.bin, base=2), int(d.bin, base=2))
            f = unsigned32(bin(f + (f<0)*pow(2, 32))[2:])
            
            # apply series of required additions mod 2^64
            f = add_modulo([f, M_list[index_list[i]], K_list[i], a])
            
            # reassign buffers
            a = +d
            d = +c
            c = +b
            
            # apply shift
            shifted = unsigned32(f.bin[S_list[i]:] + f.bin[:S_list[i]])
            b = add_modulo([b, shifted])
            
        # reassign initialisation buffers for next 512-bit chunk
        a = add_modulo([a0, a])
        b = add_modulo([b0, b])
        c = add_modulo([c0, c])
        d = add_modulo([d0, d])
        
    # once string is completely parsed, output resulting buffers in hexadecimal format
    MD5_hash_hex = ''
    for num in [a, b, c, d]:
        MD5_hash_bin = unsigned32(flip_byte_order(num.bin))
        MD5_hash_hex += MD5_hash_bin.hexa()
    
    return MD5_hash_hex

def Day4_Part1(filename='Inputs/Day4_Inputs.txt'):
    """
    Calculates the lowest positive integer which, when appended to a string key given in an
    input file and input into an MD5 hashing algorithm, returns a hash which starts with
    five zeros in hexadecimal format.

    Parameters
    ----------
    filename : str, optional
        The input file containing the key.
        The default is 'Inputs/Day4_Inputs.txt'.

    Returns
    -------
    i : int
        The lowest integer which returns an MD5 hash starting with at least 5 zeros in
        hexadecimal format, when appended to the given key.

    """
    file = open(filename)
    key = []
    for line in file:
        line = line.strip()
        line = shlex.split(line)
        if len(line) > 0:
            key = line[0]
    file.close()
    
    i = 0
    cipher = MD5()
    while not cipher.hash(key + str(i)).startswith('00000'):
        i += 1
        
    return i

def Day4_Part1a(filename='Inputs/Day4_Inputs.txt'):
    """
    Calculates the lowest positive integer which, when appended to a string key given in an
    input file and input into an MD5 hashing algorithm, returns a hash which starts with
    five zeros in hexadecimal format.
    
    (Using in-built Python library function for MD5 algorithm since mine is too slow.)

    Parameters
    ----------
    filename : str, optional
        The input file containing the key.
        The default is 'Inputs/Day4_Inputs.txt'.

    Returns
    -------
    i : int
        The lowest integer which returns an MD5 hash starting with at least 5 zeros in
        hexadecimal format, when appended to the given key.

    """
    file = open(filename)
    key = []
    for line in file:
        line = line.strip()
        line = shlex.split(line)
        if len(line) > 0:
            key = line[0]
    file.close()
    
    i = 0
    tester = str(key) + str(i)
    cipher = md5(tester.encode('utf-8'))
    while not cipher.hexdigest().startswith('00000'):
        i += 1
        tester = str(key) + str(i)
        cipher = md5(tester.encode('utf-8'))
    
    return i

def Day4_Part2(filename='Inputs/Day4_Inputs.txt'):
    """
    Calculates the lowest positive integer which, when appended to a string key given in an
    input file and input into an MD5 hashing algorithm, returns a hash which starts with
    six zeros in hexadecimal format.

    Parameters
    ----------
    filename : str, optional
        The input file containing the key.
        The default is 'Inputs/Day4_Inputs.txt'.

    Returns
    -------
    i : int
        The lowest integer which returns an MD5 hash starting with at least 6 zeros in
        hexadecimal format, when appended to the given key.

    """
    file = open(filename)
    key = []
    for line in file:
        line = line.strip()
        line = shlex.split(line)
        if len(line) > 0:
            key = line[0]
    file.close()
    
    i = 0
    cipher = MD5()
    while not cipher.hash(key + str(i)).startswith('000000'):
        i += 1
        
    return i

def Day4_Part2a(filename='Inputs/Day4_Inputs.txt'):
    """
    Calculates the lowest positive integer which, when appended to a string key given in an
    input file and input into an MD5 hashing algorithm, returns a hash which starts with
    six zeros in hexadecimal format.
    
    (Using in-built Python library function for MD5 algorithm since mine is too slow.)

    Parameters
    ----------
    filename : str, optional
        The input file containing the key.
        The default is 'Inputs/Day4_Inputs.txt'.

    Returns
    -------
    i : int
        The lowest integer which returns an MD5 hash starting with at least 6 zeros in
        hexadecimal format, when appended to the given key.

    """
    file = open(filename)
    key = []
    for line in file:
        line = line.strip()
        line = shlex.split(line)
        if len(line) > 0:
            key = line[0]
    file.close()
    
    i = 0
    tester = str(key) + str(i)
    cipher = md5(tester.encode('utf-8'))
    while not cipher.hexdigest().startswith('000000'):
        i += 1
        tester = str(key) + str(i)
        cipher = md5(tester.encode('utf-8'))
    
    return i
