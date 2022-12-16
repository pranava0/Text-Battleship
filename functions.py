import class_types

def allDestroyed(receiver : class_types.Player) -> bool:
    shiplist = receiver.Placement.shiplist
    for ship in shiplist:
        for coordinate in ship.cords:
            if (ship.orient == "vertical"):
                if (receiver.Placement.board[coordinate][ship.cords[coordinate]] != "X"):
                    return False
            elif (ship.orient == "horizontal"):
                if (receiver.Placement.board[ship.cords[coordinate]][coordinate] != "X"):
                    return False
    return True

def sunk(fire_row : int, fire_col : int, receiver : class_types.Player) -> bool:
    hit_ship = class_types.Ship()
    for ship in receiver.Placement.shiplist:
        if ((ship.orient == "vertical" and (fire_row in ship.cords) and ship.cords[fire_row] == fire_col) or (ship.orient == "horizontal" and (fire_col in ship.cords) and ship.cords[fire_col] == fire_row)):
            hit_ship = ship
            break
    for i in hit_ship.cords:
        if (hit_ship.orient == "vertical" and receiver.Placement.board[i][hit_ship.cords[i]] != "X"):
            return False
        elif (hit_ship.orient == "horizontal" and receiver.Placement.board[hit_ship.cords[i]][i] != "X"):
            return False
    
    return True

def fire(attacker : class_types.Player, receiver : class_types.Player) -> bool:
    attacker.Firing.printboard()
    attacker.Placement.printboard()

    loc = input(attacker.name + ", enter the location you want to fire at in the form row col: ")
    while (not validFire(loc, receiver)):
        loc = input(attacker.name + ", enter the location you want to fire at in the form row col: ")

    fire_row = int(loc[0])
    fire_col = int(loc[2])


    ship_name = receiver.Placement.board[fire_row][fire_col]
    if ship_name != "*" and ship_name != "O":    
        receiver.Placement.board[fire_row][fire_col] = "X"
        attacker.Firing.board[fire_row][fire_col] = "X"
        print(attacker.name + " hit " + receiver.name + "'s " + ship_name + "!")

        if sunk(fire_row, fire_col, receiver):
            print(attacker.name + " destroyed " + receiver.name + "'s " + ship_name + "!")
            if (allDestroyed(receiver)):
                attacker.Firing.printboard()
                attacker.Placement.printboard()
                print(attacker.name + " won!")
                return True

    else:
        attacker.Firing.board[fire_row][fire_col] = "O"
        receiver.Placement.board[fire_row][fire_col] = "O"
        print(attacker.name + " missed.")

        return False
    
def placeships(player : class_types.Player, ships : dict) -> None:
    player.Placement.printboard()
    for i in ships:
        while True:
            orient = input(player.name + ", enter the orientation of your " + i + ", which is " + str(ships[i]) + " long: ").lower()
            while("vertically".find(orient) != 0 and "horizontally".find(orient) != 0):
                orient = input(player.name + ", enter the orientation of your " + i + ", which is " + str(ships[i]) + " long: ").lower()
            if ("vertically".find(orient) == 0):
                orient = "vertical"
            else:
                orient = "horizontal"
            location = input("Enter the starting location for your " + i + ", which is " + str(ships[i]) + " long, in the form row col: ")
            if(len(location) == 3 and location[0].isnumeric() and location[2].isnumeric() and location[1] == " " and isValidLocation(int(location[0]), int(location[2]), i, int(ships[i]), orient, player.Placement)):
                break            
        
        player.Placement.printboard()

def isValidLocation(place_row : int, place_col : int, ship_name : str, length : int, orient : str, Placement : class_types.Placement) -> bool:
    if orient == "vertical":
        if (place_col in range(Placement.cols) and place_row in range(Placement.rows) and (length + place_row - 1) in range(Placement.rows)):
            for i in range(place_row, (place_row + length)):
                if Placement.board[i][place_col] != "*":
                    return False

            new_ship = class_types.Ship(orient, ship_name, (str(place_row) + " " + str(place_col)), length)
            for i in range(place_row, (place_row + length)):
                Placement.board[i][place_col] = ship_name
                new_ship.cords[i] = place_col
            Placement.shiplist.append(new_ship)
            return True
        else:
            return False
    elif orient == "horizontal":
        if (place_col in range(Placement.cols) and (place_col + length - 1) in range(Placement.cols) and place_row in range(Placement.rows)):
            for i in range(place_col, (place_col + length)):
                if Placement.board[place_row][i] != "*":
                    return False

            new_ship = class_types.Ship(orient, ship_name, (str(place_row) + " " + str(place_col)), length)
            for i in range(place_col, (place_col + length)):
                Placement.board[place_row][i] = ship_name
                new_ship.cords[i] = place_row
            Placement.shiplist.append(new_ship)
            return True
        else:
            return False

def validFire(fire_loc : str, receiver : class_types.Player) -> bool:
    if (len(fire_loc) != 3 or not fire_loc[0].isnumeric() or not fire_loc[2].isnumeric() or not fire_loc[1] == " "):
        return False

    fire_row = int(fire_loc[0])
    fire_col = int(fire_loc[2])

    if (fire_row not in range(receiver.Placement.rows) and fire_col not in range(receiver.Placement.cols)):
        return False

    if(receiver.Placement.board[fire_row][fire_col] == "O"):
        return False

    return True


    