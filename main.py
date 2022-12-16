import functions
import class_types

def read_config(game_configs : str) -> dict:
    configs_file = open(game_configs)
    contents = configs_file.read().splitlines()
    setup = dict()
    ship_dict = dict()
    setup['rows'] = int(contents[0])
    setup['cols'] = int(contents[1])
    setup['count'] = int(contents[2])
    for i in range(3, len(contents)):
        ship_dict[contents[i][0]] = int(contents[i][2])
    setup['ships'] = dict(sorted(ship_dict.items()))

    configs_file.close()
    return setup

def battleship_loop():
    configs = read_config(input("Please enter the path to the configuration file for this game: "))

    p1_name = input("Player 1, please enter your name: ")
    p2_name = input("Player 2, please enter your name: ")
    player1 = class_types.Player(p1_name, configs)
    player2 = class_types.Player(p2_name, configs)
    
    functions.placeships(player1, configs['ships'])
    functions.placeships(player2, configs['ships'])

    game_over = False

    while not game_over:
        game_over = functions.fire(player1, player2)
        if (game_over):
            break
        game_over = functions.fire(player2, player1)

if __name__ == "__main__":
    battleship_loop()