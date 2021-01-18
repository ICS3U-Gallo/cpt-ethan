# MONOPOLY WITH A TWIST - By Ethan Lam

from typing import List, Any
import random


first_loop = True

def main():
    game_title = "MONOPOLY WITH A TWIST!"
    coloured_game_title = ""
    i = 0
    while i < len(game_title):
        if i % 3 == 0:
            coloured_game_title += add_colour(game_title[i], "red", True)
        elif i % 3 == 1:
            coloured_game_title += add_colour(game_title[i], "orange", True)
        else:
            coloured_game_title += add_colour(game_title[i], "cyan", True)
        i += 1

    print(add_colour("     Welcome to", "none", True))
    print(coloured_game_title)
    print()
    menu_options()


def menu_options() -> None:
    """Displays available menu options for the player and handles choice.
    
    Done by: Ethan Lam
    """
    while True:
        print("[1] Start the game")
        print("[2] Read the rules")

        choice = input("> ")

        if choice == "1":
            start_game()
        elif choice == "2":
            print_rules()
        else:
            print("Invalid option!")
            print()


def start_game() -> None:
    """Starts the game
    
    Done by: Ethan Lam
    """
    players = set_up_game()
    if players == None:
        return
    
    grids = set_up_grids()

    display_board(players, grids)
    roll_dice(players)

    while True:
        clear_screen()
        display_board(players, grids)
        follow_up(players, grids)
        display_board(players, grids)
        roll_dice(players)


def set_up_grids() -> List[Any]:
    """A fixed initial set-up of the interactive grids on the board.
    
    Returns:
        The interactive grid set-up, each with unique properties.
    
    Done by: Ethan Lam
    """
    grids = []
    grid_names = ["GO", "Belleville", "North Bay", "Chance Card", "Grande Prairie", "Saint John",
    "Chance Card", "Sarnia", "Prince George", "Free Parking", "Peterborough", "Victoria", "Kamloops",
    "Chance Card", "Pay Money", "Thunder Bay", "25 dollars", "St. John's", "JAIL", "50 dollars",
    "Oshawa", "Kitchener", "Saskatoon", "Chance Card", "Vaughan", "Quebec City", "Mississauga",
    "Cell", "Vancouver", "Ottawa", "75 dollars", "Calgary", "an extra roll", "Montreal", "Pay Money",
    "Toronto"]
    unpurchaseable_grids = [0, 3, 6, 9, 13, 14, 16, 18, 19, 23, 27, 30, 32, 34]
    grid_initial_costs = [-1, 50, 50, -1, 50, 75, -1, 75, 75, -1, 100, 100, 125, -1,
    -1, 125, -1, 150, -1, -1, 150, 175, 175, -1, 175, 200, 200, -1, 250, 250, -1, 275, -1,
    300, -1, 350]
    grid_starting_worths = [-1, 10, 10, -1, 10, 20, -1, 20, 20, -1, 30, 30, 40, -1,
    -1, 40, -1, 50, -1, -1, 50, 60, 60, -1, 60, 75, 75, -1, 100, 100, -1, 125, -1,
    130, -1, 150]
    grid_special_chars = [chr(5), chr(6), chr(7), chr(14), chr(15), chr(16), chr(17), chr(18),
    chr(19), chr(20), chr(21), chr(22), chr(23), chr(24), chr(25), chr(26), chr(28),
    chr(29), chr(30), chr(31), chr(127), chr(128), chr(129), chr(130), chr(131), chr(134),
    chr(135), chr(136), chr(137), chr(138), chr(139), chr(140), chr(141), chr(142), chr(143), chr(144)]
    placements = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 273, 386, 499, 612, 725, 838,
    951, 1064, 1282, 1277, 1272, 1267, 1262, 1257, 1252, 1247, 1242, 1237, 1009, 896, 783,
    670, 557, 444, 331, 218]

    i = 0
    while i < 36:
        boolean = True
        if i in unpurchaseable_grids:
            boolean = False

        grid_name = grid_names[i]
        initial_cost = grid_initial_costs[i]
        starting_worth = grid_starting_worths[i]
        special_char = grid_special_chars[i]
        placement = placements[i]

        if 0 <= i <= 9:
            upgrade_cost = 50
        elif 10 <= i <= 18:
            upgrade_cost = 100
        elif 19 <= i <= 27:
            upgrade_cost = 150
        else:
            upgrade_cost = 200

        grid = {
            "name": grid_name,
            "belongs_to": -1,
            "communities": 0,
            "purchaseable": boolean,
            "initial_cost": initial_cost,
            "upgrade_cost": upgrade_cost,
            "worth": starting_worth,
            "special_char": special_char,
            "placement": placement
        }
        grids.append(grid)
        i += 1
    
    return grids


def follow_up(player_info: List[Any], grid_info: List[Any]) -> None:
    """Changes information about the player based on their decisions of what to do next.

    Args:
        player_info: Information about each player.
        grid_info: Information about each grid.
    
    Done by: Ethan Lam
    """
    i = 0
    while i < len(player_info):
        if player_info[i]["player_turn"]:
            break
        i += 1
    name = player_info[i]["name"]
    grid = player_info[i]["grid_pos"]
    grid_name = grid_info[grid]["name"]
    if grid_info[grid]["purchaseable"] and (grid_info[grid]["belongs_to"] == -1 or grid_info[grid]["belongs_to"] == i):
        while True:
            print()
            print("[1] Yes")
            print("[2] No")

            choice = input("> ")
            if choice == "1":
                if grid_info[grid]["belongs_to"] == -1:
                    if player_info[i]["money"] - grid_info[grid]["initial_cost"] >= 0:
                        player_info[i]["money"] -= grid_info[grid]["initial_cost"]
                        grid_info[grid]["belongs_to"] = i
                        clear_screen()
                        print(f"{name} has successfully purchased {grid_name}!")
                        break
                    else:
                        print("Not enough money!")
                else:
                    if player_info[i]["money"] - grid_info[grid]["upgrade"] >= 0:
                        player_info[i]["money"] -= grid_info[grid]["upgrade"]
                        grid_info[grid]["communities"] += 1
                        print(f"{name} has added a community to {grid_name}!")
                        clear_screen()
                        break
                    else:
                        print("Not enough money!")
            elif choice == "2":
                clear_screen()
                break
            else:
                print("Invalid option.")


    player_info[i]["player_turn"] = False

    i += 1
    if i >= len(player_info):
        i -= len(player_info)
    player_info[i]["player_turn"] = True


def clear_screen() -> None:
    """Clears the entire screen.

    Done by: Ethan Lam
    """
    print("\n" * 100)


def roll_dice(player_information: List[Any]) -> None:
    """Changes information about the player based on their dice roll.

    Args:
        player_info: Information about each player.
    
    Done by: Ethan Lam
    """
    i = 0
    while i < len(player_information):
        if player_information[i]["player_turn"]:
            break
        i += 1
    
    print()
    print("It is now " + player_information[i]["name"] + "'s turn.")
    print("You can choose to roll 1, 2, or 3 dice.")
    print("For every additional dice after 1, it costs $50 more.")
    while True:
        while True:
            try:
                number_of_rolls = int(input("Please enter the number of dice you want to roll: "))
                if number_of_rolls < 1 or number_of_rolls > 3:
                    raise ValueError
                break
            except ValueError:
                print("Invalid choice - you must roll at least 1 dice, maximum of 3.")
                print()
        
        if player_information[i]["money"] - 50 * (number_of_rolls - 1) >= 0:
            player_information[i]["money"] -= 50 * (number_of_rolls - 1)
            break
        else:
            print("Not enough money!")
            print()
    
    roll = 0
    j = 0
    while j < number_of_rolls:
        number = random.randint(1, 6)
        roll += number
        j += 1

    player_information[i]["roll"] = roll

    player_information[i]["grid_pos"] += roll
    if player_information[i]["grid_pos"] >= 36:
        player_information[i]["grid_pos"] -= 36
        player_information[i]["money"] += 200
        player_information[i]["passed_go"] = True


def set_up_game() -> List[Any]:
    """The initial set-up with features determined by the user.
    
    Returns:
        The player and game set-up.
    
    Done by: Ethan Lam
    """
    print()
    number_of_players = 0
    players = []

    print("Enter 'b' to go back to the menu.")
    
    while True:
        choice = input("Please enter the number of players (2 to 4): ")
        if choice == "b":
            print()
            return
        try:
            number_of_players = int(choice)
            if number_of_players > 4 or number_of_players < 2:
                raise ValueError
            break
        except ValueError:
            print("Invalid option!")
            print()
    print()
    print("Please enter the amount of money each player starts with (recommended: 500)")
    starting_money = get_positive_integer("> ")
    
    colour_list = ["blue", "green", "orange", "red"]

    used_names = []
    i = 0
    while i < number_of_players:
        print()
        player_name = ""
        while True:
            player_name = input(f"Please enter player {i + 1}'s name: ")
            if player_name in used_names:
                print("Name already used - please choose another name.")
                print()
            elif len(player_name) < 11:
                used_names.append(player_name)
                break
            else:
                print("MAX 10 characters.")
                print()

        print()
        while True:
            
            print(f"Which colour will {player_name} be using?")
            j = 0
            while j < len(colour_list):
                print(f"[{j + 1}] {colour_list[j]}")
                j += 1
            
            try:
                choice = int(input("> "))
                if choice > len(colour_list) or choice < 1:
                    raise ValueError
                break
            except ValueError:
                print("Invalid option.")
                print()

        player_colour = colour_list[choice - 1]
        colour_list.remove(player_colour)

        print()
        while True:
            print(f"Which gamepiece will {player_name} be using?")
            print("This must be a single character.")
        
            choice = input("> ")

            if len(choice) == 1:
                break
            else:
                print("Invalid choice - please enter just 1 character.")
                print()
            
        player_gamepiece = choice
        player_final = add_background(player_gamepiece, player_colour)

        if i == 0:
            special_character = chr(0)
        elif i == 1:
            special_character = chr(1)
        elif i == 2:
            special_character = chr(2)
        else:
            special_character = chr(3)

        player = {
            "money": starting_money,
            "cities": [],
            "player_turn": False,
            "roll": 0,
            "grid_pos": 0,
            "name": player_name,
            "colour": player_colour,
            "gamepiece": player_gamepiece,
            "visual": player_final,
            "char_representation": special_character,
            "passed_go": False
        }
        players.append(player)
        i += 1
    
    players[0]["player_turn"] = True
    print_player_settings(players)

    return players


def print_player_settings(player_info: List[Any]) -> None:
    """Prints the settings set by the user.

    Args:  
        player_info: A list of the player's settings.
    
    Done by: Ethan Lam
    """
    spacing = 0
    if len(player_info) == 2:
        spacing = " " * 7
    elif len(player_info) == 3:
        spacing = " " * 17
    else:
        spacing = " " * 29

    settings = add_colour(spacing + "PLAYER SETTINGS", "none", True)
    print()
    print(settings)

    # Prints the player settings:
    subtitles = ""
    names = ""
    player_colours = ""
    player_gamepieces = ""
    visuals_on_board = ""
    i = 0
    while i < len(player_info):
        subtitle = add_colour(f"Player {i + 1}", "none", True)
        subtitles += subtitle + " " * 13
        names += "Name: " + player_info[i]["name"] + " " * (15 - len(player_info[i]["name"]))
        player_colours += "Colour: " + player_info[i]["colour"] + " " * (13 - len(player_info[i]["colour"]))
        player_gamepieces += "Gamepiece: " + player_info[i]["gamepiece"] + " " * 9
        visuals_on_board += "Visuals: " + player_info[i]["visual"] + " " * 11
        i += 1

    print(subtitles.strip(" "))
    print(names.strip(" "))
    print(player_colours.strip(" "))
    print(player_gamepieces.strip(" "))
    print(visuals_on_board.strip(" "))
    print()


def display_board(new_player_info: List[Any], grid_info: List[Any]) -> None:
    """Displays the updated board.

    Args:
        new_player_info: Updated information about the players and the game.
        grid_info: Information about the purpose of each grid.

    Done by: Ethan Lam
    """
    i = 0
    while i < len(new_player_info):
        if new_player_info[i]["player_turn"]:
            break
        i += 1
    name = new_player_info[i]["name"]
    roll = new_player_info[i]["roll"]
    global first_loop
    if first_loop:
        roll_str = center_board_text(f"To begin, {name} must first roll.")
    elif roll == 0:
        roll_str = center_board_text(f"Now, {name} must roll.")
    else:
        roll_str = center_board_text(f"{name} rolled a {roll}.")
    
    players_money = []
    for j in range(4):
        players_money.append(center_board_text(""))
    
    j = 0
    while j < len(new_player_info):
        temp_name = new_player_info[j]["name"]
        temp_money = new_player_info[j]["money"]
        temp_visuals = new_player_info[j]["char_representation"]
        players_money[j] = center_board_text(f"{temp_visuals} {temp_name}'s money: ${temp_money}")
        j += 1

    add_200 = center_board_text("")
    if new_player_info[i]["passed_go"]:
        add_200 = center_board_text(f"{name} passed GO! You got $200!")
        new_player_info[i]["passed_go"] = False

    placements = grid_to_string_pos(new_player_info)

    grid = new_player_info[i]["grid_pos"]
    grid_name = grid_info[grid]["name"]
    landed_on = center_board_text("")
    if grid_name == "Chance Card":
        landed_on = center_board_text(f"You landed on a {grid_name}.")
    elif grid_name == "Pay Money":
        landed_on = center_board_text(f"You landed on a reserved area.")
    elif grid == 16 or grid == 19 or grid == 30 or grid == 32:
        landed_on = center_board_text(f"You get {grid_name}!")
    elif grid_name == "JAIL":
        landed_on = center_board_text(f"GO TO {grid_name}!")
    elif roll != 0:
        landed_on = center_board_text(f"You landed on {grid_name}.")

    belongs_to = grid_info[grid]["belongs_to"]
    worth = grid_info[grid]["worth"]
    question = center_board_text("")
    if grid_info[grid]["purchaseable"]:
        if belongs_to == -1:
            question = center_board_text("Would you like to buy this city?")
        elif belongs_to == i:
            question = center_board_text("Would you like to build a community?")
        else:
            question = center_board_text(f"You paid Player {belongs_to + 1} ${worth}")

    board = f"""     GO   NA   NA   CC   NA   NA   CC   NA   NA   FP
   ---------------------------------------------------
   |    |    |    |    |    |    |    |    |    |    |
   ---------------------------------------------------
NA |    |                                       |    | NA
   ------{roll_str}------
PM |    |{add_200}|    | NA
   ------{landed_on}------
NA |    |{question}|    | NA
   ------                                       ------
ER |    |                                       |    | CC
   ------                                       ------
NA |    |                                       |    | PM
   ------                                       ------
75 |    |{players_money[0]}|    | NA
   ------{players_money[1]}------
NA |    |{players_money[2]}|    | 25
   ------{players_money[3]}------
NA |    |                                       |    | NA
   ---------------------------------------------------
   |    |    |    |    |    |    |    |    |    |    |
   ---------------------------------------------------
     CL   NA   NA   NA   CC   NA   NA   NA   50   JL"""
    
    i = 0
    while i < len(placements):
        board = board[:placements[i]] + new_player_info[i]["char_representation"] + board[placements[i] + 1:]
        i += 1

    i = 0
    while i < len(grid_info):
        if grid_info[i]["belongs_to"] != -1:
            board = board[:grid_info[i]["placement"]] + grid_info[i]["special_char"] * 2 + board[grid_info[i]["placement"] + 2:]
        i += 1
    
    j = 0
    while j < 2 * len(new_player_info):
        i = 0
        while i < len(board):
            if board[i] == chr(0):
                board = board[:i] + new_player_info[0]["visual"] + board[i + 1:]
                break
            elif board[i] == chr(1):
                board = board[:i] + new_player_info[1]["visual"] + board[i + 1:]
                break
            elif board[i] == chr(2):
                board = board[:i] + new_player_info[2]["visual"] + board[i + 1:]
                break
            elif board[i] == chr(3):
                board = board[:i] + new_player_info[3]["visual"] + board[i + 1:]
                break
            i += 1
        j += 1

    change = True
    while change is True:
        change = False
        i = 0
        while i < len(board):
            j = 0
            while j < len(grid_info):
                if board[i] == grid_info[j]["special_char"]:
                    colour = new_player_info[grid_info[j]["belongs_to"]]["colour"]
                    string = add_background("NA", colour)
                    board = board[:i] + string + board[i + 2:]
                    change = True
                    break
                j += 1
            i += 1

    first_loop = False
    print()
    print(board)


def grid_to_string_pos(player_info: List[Any]) -> List[int]:
    """Converts the player's grid position to a string position on the board.

    Args:
        player_info: Information necessary to determine the positions of the players.

    Returns:
        Numbers indicating where to slice the string on the board to place each player.
    
    Done by: Ethan Lam
    """
    new_list = []
    i = 0
    while i < len(player_info):
        if player_info[i]["grid_pos"] < 10:
            new_list.append(112 + player_info[i]["grid_pos"] * 5 + i)
        elif player_info[i]["grid_pos"] < 19:
            new_list.append(154 + (player_info[i]["grid_pos"] - 9) * 113 + i)
        elif player_info[i]["grid_pos"] < 28:
            new_list.append(1171 - (player_info[i]["grid_pos"] - 18) * 5 + i)
        elif player_info[i]["grid_pos"] < 36:
            new_list.append(1126 - (player_info[i]["grid_pos"] - 27) * 113 + i)
        i += 1
    return new_list


def center_board_text(text: str) -> str:
    """Centers a string between the two edges of the board.

    Args:
        text: The string being centered.
    
    Returns:
        The centered string with the appropriate number of spaces in front.
    
    Done by: Ethan Lam
    """
    new_string = ""
    width = 39 - len(text)
    i = 0
    while i < width // 2:
        new_string += " "
        i += 1
    new_string += text + new_string
    if len(text) % 2 == 0:
        new_string += " "
    return new_string


def get_positive_integer(question: str) -> int:
    """Gets a positive integer.
 
    Args:
        question: The question used to get the user to input the integer.
 
    Returns:
        A positive integer.

    Done by: Ethan Lam
    """
    while True:
        try:
            positive_integer = int(input(question))
            if positive_integer < 0 or positive_integer > 5000:
                raise ValueError
            return positive_integer
        except ValueError:
            print("INVALID INPUT - enter a positive integer between 0 and 5000.")
            print()


def print_rules() -> None:
    """Prints out the rules of the game
    
    Done by: Ethan Lam
    """
    title = add_colour("      MONOPOLY WITH A TWIST      ", "red", True)
    print()
    print(title)
    print("---------------------------------")


def add_colour(text: str, colour: str, bold: bool) -> str:
    """Adds colour and bold to a specified text.

    Args:
        text: The text being modified.
        colour: The colour it is being changed to.
        bold: Whether the text is bolded or not.
    
    Returns:
        The original string with added colour and modifications.
    
    Done by: Ethan Lam
    """
    colours = ["red", "green", "orange", "blue", "none", "cyan"]
    code_bold = ""
    default = "\033[0;0;0m"
    if bold:
        code_bold = "1"
    else:
        code_bold = "0"

    respective_codes = [f"\033[{code_bold};31;1m", f"\033[{code_bold};32;1m",
    f"\033[{code_bold};33;1m", f"\033[{code_bold};34;1m", f"\033[{code_bold};0;1m",
    f"\033[{code_bold};36;1m"]

    i = 0
    while i < len(colours):
        if colour == colours[i]:
            break
        i += 1
    
    return respective_codes[i] + text + default


def add_background(text: str, colour: str) -> str:
    """Adds a background to a specified text.

    Args:
        text: The text being modified.
        colour: The colour the background is being changed to.
    
    Returns:
        The original string with added background colour.
    
    Done by: Ethan Lam
    """
    colours = ["red", "green", "orange", "blue"]
    default = "\033[0;0;0m"

    respective_codes = ["\033[0;37;41m", "\033[0;30;42m",
    "\033[0;37;43m", "\033[0;37;44m"]

    i = 0
    while i < len(colours):
        if colour == colours[i]:
            break
        i += 1
    
    return respective_codes[i] + text + default


if __name__ == "__main__":
    main()
