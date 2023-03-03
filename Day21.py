from itertools import combinations

def battle(player1, player2):
    """
    Determines who would win a battle between two players with a given amount of hit points,
    damage and armor, and where players take it in turns beginning with player 1 to do their
    amount of damage to the other player, minus the other player's armor down to a minimum of 1.
    The fight ends when either player's health falls to or below zero, at which point the other
    player wins the fight.

    Parameters
    ----------
    player1 : dict('Hit Points': int, 'Damage': int, 'Armor': int)
        The first player.
    player2 : dict('Hit Points': int, 'Damage': int, 'Armor': int)
        The second player.

    Returns
    -------
    victor : int
        The index of the winning player (0 or 1).

    """
    # Create copies of player data
    players = [player1.copy(), player2.copy()]
    # Player 1 goes first
    turn = 0
    while players[turn]['Hit Points'] > 0: # While both players have health
        d, a = players[turn]['Damage'], players[~turn%2]['Armor']
        # Do at least one damage, up to current player's damage - other player's health
        players[~turn%2]['Hit Points'] -= max(1, d - a)
        # Invert turn number (0 --> 1, 1 --> 0)
        turn = ~turn%2

    # Victor is whoever had the last go
    victor = ~turn%2
    return victor

def Day21_Part1(boss='Inputs/Day21_Inputs.txt', shop='Inputs/Day21_Shop.txt'):
    """
    Calculates the least amount of gold you can spend in a game and still win the fight against
    the boss, whose hit points, damage and armor are given in an input file. The player begins
    with 100 hit points, 0 damage and 0 armor, and can increase their damage and armor by spending
    gold at a shop, whose content is given in another input file, to buy items which enhance their
    properties.

    Battle Rules
    ------------
    Players take it in turns to do their amount of damage to the other player, minus the other
    player's armor down to a minimum of 1. The fight ends when either player's health falls to
    or below zero, at which point the other player wins the fight. The player goes first, followed
    by the boss.

    Parameters
    ----------
    boss : str, optional
        Input file giving the properties of the boss.
        The default is 'Inputs/Day21_Inputs.txt'.

    shop : str, optional
        Input file giving the contents of the shop.
        The default is 'Inputs/Day21_Shop.txt'.

    Returns
    -------
    min_win_cost : int
        The least amount of gold you can spend and still win the fight.

    """
    # Parse boss input file
    boss = {line.strip().split(': ')[0]: int(line.strip().split(': ')[1])
            for line in open(boss)}
    # Parse shop input file
    file = open(shop)
    shop = {}
    for line in file:
        line = line.strip().split()
        if len(line) > 0:
            if line[1] == 'Cost':
                # Start list of new item category
                category = line[0][:-1]
                shop[category] = []
            else:
                # Add item with given properties to category
                shop[category].append({'Cost': int(line[1]), 'Damage': int(line[2]),
                                       'Armor': int(line[3])})
    file.close()

    # Inialise player with base properties
    base_player = {'Hit Points': 100, 'Damage': 0, 'Armor': 0}
    costs = [[], []]

    # Loop though every possible weapon
    for weapon in shop['Weapons']:
        # Loop through every possible armor (adding None as an option)
        for armor in shop['Armor'] + [None]:
            ## First account for if no rings are bought:
            # Apply weapon and armor properties to player and add up cost
            player = base_player.copy()
            player['Damage'] += weapon['Damage']
            cost = 1*weapon['Cost']
            if armor:
                player['Armor'] += armor['Armor']
                cost += armor['Cost']
            # Simulate battle
            victor = battle(player, boss)
            # Add cost to costs[0] if player wins, costs[1] if boss wins/player loses
            costs[victor].append(cost)
            ## Now account for if any rings are bought:
            for r in range(1, 3): # Player can buy r = 1 or 2 rings
                for rings in combinations(shop['Rings'], r): # Choose r rings from the options
                    # Start at player/cost after selected weapon and armor are applied
                    ringed_cost = 1*cost
                    ringed_player = player.copy()
                    # Apply ring properties to player and add up cost
                    for ring in rings:
                        ringed_player['Damage'] += ring['Damage']
                        ringed_player['Armor'] += ring['Armor']
                        ringed_cost += ring['Cost']
                        # Simulate battle
                    victor = battle(ringed_player, boss)
                    # Add cost to costs[0] if player wins, costs[1] if boss wins
                    costs[victor].append(ringed_cost)

    # Find minimum cost where player won
    min_win_cost = min(costs[0])

    return min_win_cost

def Day21_Part2(boss='Inputs/Day21_Inputs.txt', shop='Inputs/Day21_Shop.txt'):
    """
    Calculates the most amount of gold you can spend in a game and still lose a fight against
    the boss, whose hit points, damage and armor are given in an input file. The player begins
    with 100 hit points, 0 damage and 0 armor, and can increase their damage and armor by spending
    gold at a shop, whose content is given in another input file, to buy items which enhance their
    properties.

    Battle Rules
    ------------
    Players take it in turns to do their amount of damage to the other player, minus the other
    player's armor down to a minimum of 1. The fight ends when either player's health falls to
    or below zero, at which point the other player wins the fight. The player goes first, followed
    by the boss.

    Parameters
    ----------
    boss : str, optional
        Input file giving the properties of the boss.
        The default is 'Inputs/Day21_Inputs.txt'.

    shop : str, optional
        Input file giving the contents of the shop.
        The default is 'Inputs/Day21_Shop.txt'.

    Returns
    -------
    max_lose_cost : int
        The most amount of gold you can spend and still lose the fight.

    """
    # Parse boss input file
    boss = {line.strip().split(': ')[0]: int(line.strip().split(': ')[1])
            for line in open(boss)}
    # Parse shop input file
    file = open(shop)
    shop = {}
    for line in file:
        line = line.strip().split()
        if len(line) > 0:
            if line[1] == 'Cost':
                # Start list of new item category
                category = line[0][:-1]
                shop[category] = []
            else:
                # Add item with given properties to category
                shop[category].append({'Cost': int(line[1]), 'Damage': int(line[2]),
                                       'Armor': int(line[3])})
    file.close()

    # Inialise player with base properties
    base_player = {'Hit Points': 100, 'Damage': 0, 'Armor': 0}
    costs = [[], []]

    # Loop though every possible weapon
    for weapon in shop['Weapons']:
        # Loop through every possible armor (adding None as an option)
        for armor in shop['Armor'] + [None]:
            ## First account for if no rings are bought:
            # Apply weapon and armor properties to player and add up cost
            player = base_player.copy()
            player['Damage'] += weapon['Damage']
            cost = 1*weapon['Cost']
            if armor:
                player['Armor'] += armor['Armor']
                cost += armor['Cost']
            # Simulate battle
            victor = battle(player, boss)
            # Add cost to costs[0] if player wins, costs[1] if boss wins/player loses
            costs[victor].append(cost)
            ## Now account for if any rings are bought:
            for r in range(1, 3): # Player can buy r = 1 or 2 rings
                for rings in combinations(shop['Rings'], r): # Choose r rings from the options
                    # Start at player/cost after selected weapon and armor are applied
                    ringed_cost = 1*cost
                    ringed_player = player.copy()
                    # Apply ring properties to player and add up cost
                    for ring in rings:
                        ringed_player['Damage'] += ring['Damage']
                        ringed_player['Armor'] += ring['Armor']
                        ringed_cost += ring['Cost']
                        # Simulate battle
                    victor = battle(ringed_player, boss)
                    # Add cost to costs[0] if player wins, costs[1] if boss wins
                    costs[victor].append(ringed_cost)

    # Find maximum cost where player lost
    max_lose_cost = max(costs[1])

    return max_lose_cost
