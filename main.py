tik_tak_toe_table = ["_" for i in range(9)]
current_player = ""


def start(started) -> None:
    while True:
        print_table()
        if not started:
            started = True
            while True:
                who_starts_input = input("Who should start? X or Y")
                if who_starts_input == "X":
                    current_player = "X"
                    break
                elif who_starts_input == "Y":
                    current_player = "Y"
                    break
                else:
                    print("Input is invalid!")

        else:
            check_if_someone_won(current_player)
            # Switch current player
            if current_player == "X":
                current_player = "Y"
            else:
                current_player = "X"
        while True:
            try:
                which_field = int(input("On which field do you wanna place it? From 1-9"))
                if which_field < 0 or which_field > 9:  # Check if input is valid
                    raise ValueError
                elif tik_tak_toe_table[which_field - 1] != "_":  # If field is not empty
                    raise ValueError
                else:
                    tik_tak_toe_table[which_field - 1] = current_player
                    break
            except ValueError:
                print("Give me a valid input")


def check_if_someone_won(current_player) -> None:
    if tik_tak_toe_table[0] == "X" and tik_tak_toe_table[1] == "X" and tik_tak_toe_table[2] == "X" or tik_tak_toe_table[0] == "Y" and tik_tak_toe_table[1] == "Y" and tik_tak_toe_table[2] == "Y":
        print_who_won(current_player)
    elif tik_tak_toe_table[0] == "X" and tik_tak_toe_table[4] == "X" and tik_tak_toe_table[8] == "X" or \
            tik_tak_toe_table[0] == "Y" and tik_tak_toe_table[5] == "Y" and tik_tak_toe_table[9] == "Y":
        print_who_won(current_player)
    elif tik_tak_toe_table[0] == "X" and tik_tak_toe_table[3] == "X" and tik_tak_toe_table[6] == "X" or \
            tik_tak_toe_table[0] == "Y" and tik_tak_toe_table[3] == "Y" and tik_tak_toe_table[6] == "Y":
        print_who_won(current_player)
    elif tik_tak_toe_table[1] == "X" and tik_tak_toe_table[4] == "X" and tik_tak_toe_table[8] == "X" or \
            tik_tak_toe_table[1] == "Y" and tik_tak_toe_table[4] == "Y" and tik_tak_toe_table[8] == "Y":
        print_who_won(current_player)
    elif tik_tak_toe_table[2] == "X" and tik_tak_toe_table[5] == "X" and tik_tak_toe_table[8] == "X" or \
            tik_tak_toe_table[2] == "Y" and tik_tak_toe_table[5] == "Y" and tik_tak_toe_table[8] == "Y":
        print_who_won(current_player)
    elif tik_tak_toe_table[2] == "X" and tik_tak_toe_table[4] == "X" and tik_tak_toe_table[6] == "X" or \
            tik_tak_toe_table[2] == "Y" and tik_tak_toe_table[4] == "Y" and tik_tak_toe_table[6] == "Y":
        print_who_won(current_player)
    elif "_" not in tik_tak_toe_table:
        print("Tie")
        exit()


def print_who_won(current_player) -> None:
    print(current_player, "Has won!")
    exit()

    
def print_table() -> None:
    for i in range(0, 9, 3):
        print("|".join(tik_tak_toe_table[i:i + 3]), "  ", i+1, i+2, i+3)


if __name__ == '__main__':
    start(started=False)
