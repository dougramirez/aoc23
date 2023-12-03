from collections import OrderedDict

MAX_RED_CUBES = 12
MAX_GREEN_CUBES = 13
MAX_BLUE_CUBES = 14


def is_game_possible(sets) -> bool:
    for set in sets:
        if (
            set[0] > MAX_RED_CUBES
            or set[1] > MAX_GREEN_CUBES
            or set[2] > MAX_BLUE_CUBES
        ):
            return False

    return True


def parse_game(game: str):
    game_sets = list()

    # Remove any new lines chars ('\n)
    game = game.strip()

    # Parse out the game ID number
    game_id_number = game.split("Game ")[1].split(":")[0]
    game = game.replace(f"Game {game_id_number}: ", "")

    # Parse out the game sets
    sets = game.split("; ")
    for set in sets:
        set = set.split(", ")

        red_cubes = 0
        green_cubes = 0
        blue_cubes = 0

        for pull in set:
            pull = pull.split(" ")
            if pull[1] == "red":
                red_cubes += int(pull[0])
            elif pull[1] == "green":
                green_cubes += int(pull[0])
            else:
                blue_cubes += int(pull[0])

        game_sets.append([red_cubes, green_cubes, blue_cubes])

    return game_id_number, game_sets


# Open the calibration document
games = open("./day2/games.txt", "r")
game_id_number_sum = 0
for game in games:
    game_id_number, sets = parse_game(game)
    if is_game_possible(sets):
        game_id_number_sum += int(game_id_number)

print(f"The sum of all possible game IDs is: {game_id_number_sum}")
