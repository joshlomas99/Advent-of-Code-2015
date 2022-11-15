class Ingredient:
    """
    Class describing an ingredient for cookies.
    """
    def __init__(self, name, capacity, durability, flavor, texture, calories):
        """
        Initialise the class with six parameters.

        Parameters
        ----------
        name : str
            Name of the ingredient.
        capacity : int
            How well it helps the cookie absorb milk.
        durability : int
            How well it keeps the cookie intact when full of milk.
        flavor : int
            How tasty it makes the cookie.
        texture : int
            How it improves the feel of the cookie.
        calories : int
            How many calories it adds to the cookie.
        
        Returns
        -------
        None.

        """
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories

    def __repr__(self):
        """
        Return the representation of an Ingredient object.

        Returns
        -------
        str
            Representation.

        """
        return '{}({}, {}, {}, {}, {}, {})'.format(self.__class__.__name__, self.name,
                                                   self.capacity, self.durability, self.flavor,
                                                   self.texture, self.calories)

def Day15_Part1(filename='Inputs/Day15_Inputs.txt'):
    """
    Calculates the score of the highest possible scoring cookie recipe, where a cookie can be
    comprised of any proportion of the available ingredients totalling 100 teaspoons. The total
    score of a cookie can be found by adding up each of the properties of each ingredient in the
    given proportions (negative totals become 0) and then multiplying together everything except
    calories. Ingredient properties are given in an input file.

    Parameters
    ----------
    filename : str, optional
        Input file containing the ingredient properties.
        The default is 'Inputs/Day15_Inputs.txt'.

    Returns
    -------
    max_score : int
        The score of the highest possible scoring cookie.

    """
    file = open(filename)
    ingredients = []
    for line in file:
        line = line.strip().split()
        if len(line) > 0:
            ingredients.append(Ingredient(line[0].split(':')[0], int(line[2].split(',')[0]),
                                          int(line[4].split(',')[0]),
                                          int(line[6].split(',')[0]),
                                          int(line[8].split(',')[0]),
                                          int(line[10].split(',')[0])))

    file.close()

    scores = []
    for a in range(101):
        print(a)
        for b in range(101 - a):
            for c in range(101 - a - b):
                d = 100 - (a + b + c)
                scores.append(1)
                for prop in ['capacity', 'durability', 'flavor', 'texture']:
                    prop_sum = sum([[a, b, c, d][n]*eval(f'ingredient.{prop}') for n, ingredient in enumerate(ingredients)])
                    if prop_sum < 0:
                        scores[-1] = 0
                        break
                    else:
                        scores[-1] *= prop_sum

    max_score = max(scores)

    return max_score

def Day15_Part2(filename='Inputs/Day15_Inputs.txt'):
    """
    Calculates the score of the highest possible scoring cookie recipe, where a cookie can be
    comprised of any proportion of the available ingredients totalling 100 teaspoons. The total
    score of a cookie can be found by adding up each of the properties of each ingredient in the
    given proportions (negative totals become 0) and then multiplying together everything except
    calories.  However, cookies are now also required to have exactly 500 calories in total.
    Ingredient properties are given in an input file.

    Parameters
    ----------
    filename : str, optional
        Input file containing the ingredient properties.
        The default is 'Inputs/Day15_Inputs.txt'.

    Returns
    -------
    max_score : int
        The score of the highest possible scoring cookie with exactly 500 calories.

    """
    file = open(filename)
    ingredients = []
    for line in file:
        line = line.strip().split()
        if len(line) > 0:
            ingredients.append(Ingredient(line[0].split(':')[0], int(line[2].split(',')[0]),
                                          int(line[4].split(',')[0]),
                                          int(line[6].split(',')[0]),
                                          int(line[8].split(',')[0]),
                                          int(line[10].split(',')[0])))

    file.close()

    scores = []
    for a in range(101):
        for b in range(101 - a):
            for c in range(101 - a - b):
                d = 100 - (a + b + c)
                calories = sum([[a, b, c, d][n]*ingredient.calories for n, ingredient in enumerate(ingredients)])
                if calories != 500:
                    continue
                scores.append(1)
                for prop in ['capacity', 'durability', 'flavor', 'texture']:
                    prop_sum = sum([[a, b, c, d][n]*eval(f'ingredient.{prop}') for n, ingredient in enumerate(ingredients)])
                    if prop_sum < 0:
                        scores[-1] = 0
                        break
                    else:
                        scores[-1] *= prop_sum

    max_score = max(scores)

    return max_score
