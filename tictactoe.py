print("""                                               
-------|-------|------
  x1   |  x2   |  x3 
-------|-------|------
  x4   |  x5   |  x6
-------|-------|------
  x7   |  x8   |  x9   
-------|-------|------  
""")
values_array = [0, 0, 0, 0, 0, 0, 0, 0, 0]
value_player = [" ", " ", " ", " ", " ", " ", " ", " ", " ", ]
win_condition = [0]


def choose_tiles(x):
    def match_ip():
        value_player_inp: str = input(f"Player {x} Select Tile >")
        match value_player_inp:
            case "x1":
                if values_array[0] == 0:
                    values_array[0] = x
                else:
                    print("This tile is already taken")
            case "x2":
                if values_array[1] == 0:
                    values_array[1] = x
                else:
                    print("This tile is already taken")
            case "x3":
                if values_array[2] == 0:
                    values_array[2] = x
                else:
                    print("This tile is already taken")
            case "x4":
                if values_array[3] == 0:
                    values_array[3] = x
                else:
                    print("This tile is already taken")
            case "x5":
                if values_array[4] == 0:
                    values_array[4] = x
                else:
                    print("This tile is already taken")
            case "x6":
                if values_array[5] == 0:
                    values_array[5] = x
                else:
                    print("This tile is already taken")
            case "x7":
                if values_array[6] == 0:
                    values_array[6] = x
                else:
                    print("This tile is already taken")
            case "x8":
                if values_array[7] == 0:
                    values_array[7] = x
                else:
                    print("This tile is already taken")
            case "x9":
                if values_array[8] == 0:
                    values_array[8] = x
                else:
                    print("This tile is already taken")
            case _:
                print("Sorry didn't understand you please try again.")
    value_player_inp = input(f"Player {x} Select Tile >")

    match value_player_inp:
        case "x1":
            if values_array[0] == 0:
                values_array[0] = x
            else:
                print("This tile is already taken! If you choose a taken tile again it will be the other players turn!")
                match_ip()
        case "x2":
            if values_array[1] == 0:
                values_array[1] = x
            else:
                print("This tile is already taken! If you choose a taken tile again it will be the other players turn!")
                match_ip()
        case "x3":
            if values_array[2] == 0:
                values_array[2] = x
            else:
                print("This tile is already taken! If you choose a taken tile again it will be the other players turn!")
                match_ip()
        case "x4":
            if values_array[3] == 0:
                values_array[3] = x
            else:
                print("This tile is already taken! If you choose a taken tile again it will be the other players turn!")
                match_ip()
        case "x5":
            if values_array[4] == 0:
                values_array[4] = x
            else:
                print("This tile is already taken! If you choose a taken tile again it will be the other players turn!")
                match_ip()
        case "x6":
            if values_array[5] == 0:
                values_array[5] = x
            else:
                print("This tile is already taken! If you choose a taken tile again it will be the other players turn!")
                match_ip()
        case "x7":
            if values_array[6] == 0:
                values_array[6] = x
            else:
                print("This tile is already taken! If you choose a taken tile again it will be the other players turn!")
                match_ip()
        case "x8":
            if values_array[7] == 0:
                values_array[7] = x
            else:
                print("This tile is already taken! If you choose a taken tile again it will be the other players turn!")
                match_ip()
        case "x9":
            if values_array[8] == 0:
                values_array[8] = x
            else:
                print("This tile is already taken! If you choose a taken tile again it will be the other players turn!")
            match_ip()
        case _:
            print("Sorry didn't understand you please try again.")
            match_ip()
    if values_array[0] == 1:
        value_player[0] = "O"
    elif values_array[0] == 2:
        value_player[0] = "X"
    if values_array[1] == 1:
        value_player[1] = "O"
    elif values_array[1] == 2:
        value_player[1] = "X"
    if values_array[2] == 1:
        value_player[2] = "O"
    elif values_array[2] == 2:
        value_player[2] = "X"
    if values_array[3] == 1:
        value_player[3] = "O"
    elif values_array[3] == 2:
        value_player[3] = "X"
    if values_array[4] == 1:
        value_player[4] = "O"
    elif values_array[4] == 2:
        value_player[4] = "X"
    if values_array[5] == 1:
        value_player[5] = "O"
    elif values_array[5] == 2:
        value_player[5] = "X"
    if values_array[6] == 1:
        value_player[6] = "O"
    elif values_array[6] == 2:
        value_player[6] = "X"
    if values_array[7] == 1:
        value_player[7] = "O"
    elif values_array[7] == 2:
        value_player[7] = "X"
    if values_array[8] == 1:
        value_player[8] = "O"
    elif values_array[8] == 2:
        value_player[8] = "X"

    print(f"""
        -------|-------|------
           {value_player[0]}   |   {value_player[1]}   |   {value_player[2]}  
        -------|-------|------
           {value_player[3]}   |   {value_player[4]}   |   {value_player[5]}
        -------|-------|------
           {value_player[6]}   |   {value_player[7]}   |   {value_player[8]}
        -------|-------|------""")
    if values_array[0] == values_array[1] == values_array[2]:
        if values_array[0] and values_array[1] and values_array[1] == 1:
            print("Player 1 wins")
            win_condition[0] = 1
        elif values_array[0] and values_array[1] and values_array[1] == 2:
            print("Player 2 wins")
            win_condition[0] = 1
    if values_array[0] == values_array[3] == values_array[6]:
        if values_array[0] and values_array[3] and values_array[6] == 1:
            print("Player 1 wins")
            win_condition[0] = 1
        elif values_array[0] and values_array[3] and values_array[6] == 2:
            print("Player 2 wins")
            win_condition[0] = 1
    if values_array[1] == values_array[4] == values_array[6]:
        if values_array[1] and values_array[4] and values_array[6] == 1:
            print("Player 1 wins")
            win_condition[0] = 1
        elif values_array[1] and values_array[4] and values_array[6] == 2:
            print("Player 2 wins")
            win_condition[0] = 1
    if values_array[2] == values_array[5] == values_array[8]:
        if values_array[2] and values_array[5] and values_array[8] == 1:
            print("Player 1 wins")
            win_condition[0] = 1
        elif values_array[2] and values_array[5] and values_array[8] == 2:
            print("Player 2 wins")
            win_condition[0] = 1
    if values_array[0] == values_array[4] == values_array[8]:
        if values_array[0] and values_array[4] and values_array[8] == 1:
            print("Player 1 wins")
            win_condition[0] = 1
        elif values_array[0] and values_array[4] and values_array[8] == 2:
            print("Player 2 wins")
            win_condition[0] = 1
    if values_array[2] == values_array[4] == values_array[6]:
        if values_array[2] and values_array[4] and values_array[6] == 1:
            print("Player 1 wins")
            win_condition[0] = 1
        elif values_array[2] and values_array[4] and values_array[6] == 2:
            print("Player 2 wins")
            win_condition[0] = 1
    if values_array[3] == values_array[4] == values_array[5]:
        if values_array[3] and values_array[4] and values_array[5] == 1:
            print("Player 1 wins")
            win_condition[0] = 1
        elif values_array[3] and values_array[4] and values_array[5] == 2:
            print("Player 2 wins")
            win_condition[0] = 1
    if values_array[6] == values_array[7] == values_array[8]:
        if values_array[6] and values_array[7] and values_array[8] == 1:
            print("Player 1 wins")
            win_condition[0] = 1
        elif values_array[6] and values_array[7] and values_array[8] == 2:
            print("Player 2 wins")
            win_condition[0] = 1


while True:
    if win_condition[0] == 0:
        choose_tiles(1)
    else:
        break
    if win_condition[0] == 0:
        choose_tiles(2)
    else:
        break
    if win_condition[0] == 0:
        choose_tiles(1)
    else:
        break
    if win_condition[0] == 0:
        choose_tiles(2)
    else:
        break
    if win_condition[0] == 0:
        choose_tiles(1)
    else:
        break
    if win_condition[0] == 0:
        choose_tiles(2)
    else:
        break
    if win_condition[0] == 0:
        choose_tiles(1)
    else:
        break
    if win_condition[0] == 0:
        choose_tiles(2)
    else:
        break
    if win_condition[0] == 0:
        choose_tiles(1)
    else:
        break
print("All tiles filled and still no winner...")
