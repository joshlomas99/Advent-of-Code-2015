def get_input(input_file: str='Inputs/Day22_Inputs.txt') -> dict:
    """
    Parse an input file containing the properties of the boss in a battle.

    Parameters
    ----------
    input_file : str, optional
        Input file giving the boss properties.
        The default is 'Inputs/Day22_Inputs.txt'.

    Returns
    -------
    boss : dict(str: int)
        The properties of the boss in the form {property: value}.

    """
    # Parse input file
    with open(input_file) as f:
        # Assign properties
        boss = {line.strip().split(': ')[0] : int(line.strip().split(': ')[1])\
                for line in f.readlines()}

    return boss

# Dictionary of all spells and their costs
ALL_SPELLS = {'Magic Missile': 53, 'Drain': 73, 'Shield': 113, 'Poison': 173, 'Recharge': 229}

class SpellError(Exception):
    """
    Exception class for Spell casting.
    """

    pass

def cast(spell: str, player: dict, boss: dict, active_spells: dict, curr_spend: int) -> tuple:
    """
    Processes the casting and effects of a given spell by the player.

    Parameters
    ----------
    spell : str
        Name of the spell being cast.
    player : dict(str: int)
        Player properties in the form {property: value}.
    boss : dict(str: int)
        Boss properties in the form {property: value}.
    active_spells : dict(str: int)
        Currently active spells in the form {name: time_left}.
    curr_spend : int
        Current total amount of mana spent by the player.

    Raises
    ------
    SpellError
        If an unknown spell name is cast.
    SpellError
        If a spell is cast which is already active.
    SpellError
        If the player cannot afford to cast the spell.

    Returns
    -------
    player : dict(str: int)
        Player properties in the form {property: value} after spell cost and effects.
    boss : dict(str: int)
        Boss properties in the form {property: value} after spell effects.
    active_spells : dict(str: int)
        Currently active spells in the form {name: time_left} after spell is cast.
    curr_spend : int
        Current total amount of mana spent by the player after spell cost.

    """
    # Check spell is valid
    if spell not in ALL_SPELLS:
        raise SpellError(f'Unknown spell {spell}.')
    # Check spell is not already active
    if spell in active_spells:
        raise SpellError(f'Casted spell {spell} is already active!')
    # Check player can afford spell
    if ALL_SPELLS[spell] > player['Mana']:
        raise SpellError('Player with {0} mana cannot afford this spell costing {1}!' \
                         .format(player["Mana"], ALL_SPELLS[spell]))

    # Create copies of player, boss and active spell dictionaries
    player, boss, active_spells = player.copy(), boss.copy(), active_spells.copy()
    # Apply spell cost to player and curr_spend
    player['Mana'] -= ALL_SPELLS[spell]
    curr_spend += ALL_SPELLS[spell]
    # Apply corresponding spell effects
    if spell == 'Magic Missile':
        boss['Hit Points'] -= 4
    if spell == 'Drain':
        boss['Hit Points'] -= 2
        player['Hit Points'] += 2
    # Add timed effects to active_effects with total time periods
    if spell == 'Shield':
        active_spells['Shield'] = 6
    if spell == 'Poison':
        active_spells['Poison'] = 6
    if spell == 'Recharge':
        active_spells['Recharge'] = 5

    return player, boss, active_spells, curr_spend

def active_effects(player, boss, active_spells):
    """
    Apply two turns worth of effects of any currently active spells which last multiple turns.
    This is to account for one player and boss turn each.

    Parameters
    ----------
    player : dict(str: int)
        Player properties in the form {property: value}.
    boss : dict(str: int)
        Boss properties in the form {property: value}.
    active_spells : dict(str: int)
        Currently active spells in the form {name: time_left}.

    Returns
    -------
    player : dict(str: int)
        Player properties in the form {property: value} after spell effects.
    boss : dict(str: int)
        Boss properties in the form {property: value} after spell effects.
    active_spells : dict(str: int)
        Currently active spells in the form {name: time_left} after another turn has passed.

    """
    # For each possible active spell, apply corresponding effects worth two turns
    if 'Poison' in active_spells:
        # Unless only 1 turn is left on the timer, then don't double the effect
        if active_spells['Poison'] > 1:
            boss['Hit Points'] -= 6
        else:
            boss['Hit Points'] -= 3
    if 'Recharge' in active_spells:
        if active_spells['Recharge'] > 1:
            player['Mana'] += 202
        else:
            player['Mana'] += 101

    # Remove 1 from the time left for each spell, and remove from the dictionary if the time
    # falls below 2, since we are working two turns at a time
    active_spells = {k: v-2 for k, v in active_spells.items() if v > 2}

    return player, boss, active_spells

def process_turn(player, boss, active_spells, curr_spend, curr_min, difficulty='easy'):
    """
    Performs a recursive depth-first search to find the minimum possible amount of mana which can
    be spent by a player with given properties in a battle against a boss with given properties,
    while still winning the battle.

    Battle
    ------    
    The player goes first in the battle, and turns proceed alternatively between the boss and
    player. Mana is spent by the player casting spells to damage the boss or help themselves,
    while the boss damages the player the same amount every turn. Some spells have effects which
    last multiple turns, and apply effects every turn they are active, both on player and boss
    turns. If the player cannot afford any spells on their turn, they lose. Otherwise, the first
    player to reach 0 hit points or fewer loses.

    Parameters
    ----------
    player : dict(str: int)
        Player properties in the form {property: value}.
    boss : dict(str: int)
        Boss properties in the form {property: value}.
    active_spells : dict(str: int)
        Currently active spells in the form {name: time_left}.
    curr_spend : int
        Current total amount of mana spent by the player.
    curr_min : int
        Current minimum spend found which resulted in a player victory.
    difficulty : str, optional
        Difficulty of the game, can be 'easy' or 'hard'. In 'hard' mode, the player loses 1 hit
        point every player turn.
        The default is 'easy'.

    Returns
    -------
    min_spend
        Minimum possible mana spend which can result in a player victory.

    """
    # If we have gone over the minimum spend found so far, no point continuing
    if curr_min and curr_spend >= curr_min:
        # Don't consider the current spend
        return curr_min

    # If Poison is active and boss HP is 3 or lower, boss will not survive another turn of effects
    if 'Poison' in active_spells and boss['Hit Points'] <= 3: # Player wins
        # Return minimum of current minimum found and current spend
        if not curr_min:
            return curr_spend
        return min(curr_min, curr_spend)

    # If difficulty is hard, the player loses 1 hit point at the start of every player turn
    if difficulty == 'hard':
        player['Hit Points'] -= 1

    # If the player is at or below 0 HP, they lose
    if player['Hit Points'] <= 0:
        # Don't consider the current spend
        return curr_min

    # Apply active spell effects
    player, boss, active_spells = active_effects(player, boss, active_spells)

    # If the boss HP is at or below 0, the player wins
    if boss['Hit Points'] <= 0:
        # Return minimum of current minimum found and current spend
        if not curr_min:
            return curr_spend
        return min(curr_min, curr_spend)

    # If the player cannot afford to cast any spells on their turn, they lose
    if player['Mana'] < min(ALL_SPELLS.values()):
        # Don't consider the current spend
        return curr_min

    # If boss HP is at or below 4, player can win by casting Magic Missile, which must be the
    # most efficient way since this is the cheapest spell
    if boss['Hit Points'] <= 4: # Win
        # Return minimum of current minimum found and current spend + Magic Missile cost
        if not curr_min:
            return curr_spend + ALL_SPELLS['Magic Missile']
        return min(curr_min, curr_spend + ALL_SPELLS['Magic Missile'])

    # Otherwise, continue the battle: for each spell the player can cast
    for next_spell, cost in ALL_SPELLS.items():
        # If the spell is already active, cannot cast it
        if next_spell in active_spells:
            continue
        # Skip spells the player cannot afford
        if cost > player['Mana']:
            continue

        # Cast the current next spell
        next_player, next_boss, next_act_sp, next_spend = cast(next_spell, player, boss,
                                                               active_spells, curr_spend)

        # Boss's turn: does given amount of damage, -7 if Shield spell is currently active
        next_player['Hit Points'] -= (boss['Damage'] - (7*('Shield' in next_act_sp)))

        # Recursively find the minimum possible spend from this point
        min_here = process_turn(next_player, next_boss, next_act_sp, next_spend, curr_min,
                                difficulty)

        # Set current minimum to the minimum of current minimum found and the minimum spend
        # possible here
        if min_here:
            if curr_min:
                curr_min = min(curr_min, min_here)
            else:
                curr_min = 1*min_here

    return curr_min

def Day22_Part1(input_file: str='Inputs/Day22_Inputs.txt') -> int:
    """
    Finds the minimum possible amount of mana which can be spent by a player in a battle against a
    boss, while still winning the battle. The player starts with 50 hit points and 500 mana, and
    the boss properties (damage_per_turn and hit points) are given in an input file.

    Battle
    ------    
    The player goes first in the battle, and turns proceed alternatively between the boss and
    player. Mana is spent by the player casting spells to damage the boss or help themselves,
    while the boss damages the player the same amount every turn. Some spells have effects which
    last multiple turns, and apply effects every turn they are active, both on player and boss
    turns. If the player cannot afford any spells on their turn, they lose. Otherwise, the first
    player to reach 0 hit points or fewer loses.

    Parameters
    ----------
    input_file : str, optional
        Input file giving the boss properties.
        The default is 'Inputs/Day22_Inputs.txt'.

    Returns
    -------
    min_mana : int
        The minimum possible amount of mana which can be spent by the player while still winning
        the battle.

    """
    # Parse input file to get boss properties
    boss = get_input(input_file)
    # Set initial player properties
    player = {'Hit Points': 50, 'Mana': 500}

    # Perform a recursive depth-first search to find the minimum possible mana spent while winning
    min_mana = process_turn(player, boss, dict(), 0, None)

    return min_mana

def Day22_Part2(input_file='Inputs/Day22_Inputs.txt'):
    """
    Finds the minimum possible amount of mana which can be spent by a player in a battle against a
    boss, while still winning the battle. The player starts with 50 hit points and 500 mana, and
    the boss properties (damage_per_turn and hit points) are given in an input file. However, now
    the battle is played in 'hard' difficulty mode, in which the player loses an additional 1 hit
    point every player turn.

    Battle
    ------    
    The player goes first in the battle, and turns proceed alternatively between the boss and
    player. Mana is spent by the player casting spells to damage the boss or help themselves,
    while the boss damages the player the same amount every turn. Some spells have effects which
    last multiple turns, and apply effects every turn they are active, both on player and boss
    turns. If the player cannot afford any spells on their turn, they lose. Otherwise, the first
    player to reach 0 hit points or fewer loses.

    Parameters
    ----------
    input_file : str, optional
        Input file giving the boss properties.
        The default is 'Inputs/Day22_Inputs.txt'.

    Returns
    -------
    min_mana : int
        The minimum possible amount of mana which can be spent by the player while still winning
        the battle on 'hard' difficulty.

    """
    # Parse input file to get boss properties
    boss = get_input(input_file)
    # Set initial player properties
    player = {'Hit Points': 50, 'Mana': 500}

    # Perform a recursive depth-first search to find the minimum possible mana spent while winning
    # with the difficulty set to 'hard'
    min_mana = process_turn(player, boss, dict(), 0, None, 'hard')

    return min_mana
