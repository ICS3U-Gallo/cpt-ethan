# TODO: complete laundry_room() to go back to 'basement'
# TODO: add "backyard" location. You can get to it from the basement.
#       from the backyard, you can only go back into the basement.



def main():
    game_state = [
        "basement",  # location
        [],  # player inventory
    ]


    while True:
        print("main switchboard")
        # direct to certain locations.

        location = game_state[0]
        if location == "basement":
            basement(game_state)
        elif location == "laundry_room":
            laundry_room()
        elif location == "main_floor":
            main_floor(game_state)


def basement(game_state):
    # - Decription text
    print("in the BASEMENT")

    # - Display menu options
    print("[1] go to laundry room")
    print("[2] go to main floor")

    # - get a choice
    choice = input("choice: ")

    # - handle the choice
    if choice == "1":
        inventory = game_state[1]
        if "laundry_key" in inventory:
            game_state[0] = "laundry_room"
        else:
            print("you do not have the key")
    elif choice == "2":
        game_state[0] = "main_floor"


def laundry_room():
    print("in LAUNDRY ROOM")
    input()

    # TODO: go back to BASEMENT


def main_floor(game_state):
    # complete some complex puzzle to get a key
    print("on MAIN FLOOR")
    print("NOT IMPLEMENTED. BILL DIDNT DO THEIR WORK.")
    print("Player is granted the laundry room key.")

    game_state[0] = "basement"
    game_state[1].append("laundry_key")


# if we are running this file directly (not importing it)
if __name__ == "__main__":
    main()