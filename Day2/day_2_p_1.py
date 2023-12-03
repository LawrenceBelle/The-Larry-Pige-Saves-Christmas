
from day_2_input import input
from day_2_classes import Cube, Sample, GameData


COLOURS = ["red", "green", "blue"]
MAX_VALUES = { COLOURS[0] : 12, COLOURS[1] : 13, COLOURS[2] : 14 }

def get_vaule(input: str) -> int:
    games = deconstruct_input(input)

    game_ids = list(range(1, 101))
    for game in games:
        for sample in game.samples:
            for cube in sample.cubes:
                if cube.quantity > MAX_VALUES[cube.colour]:
                    if game.id in game_ids:
                        game_ids.remove(game.id)

    return sum(game_ids)


def deconstruct_input(input: str) -> list[GameData]:
    output = []
    split_input = input.split('\n')

    for line in split_input:
        line = line[4:] # Removes "Game "
        game_number, game_data = line.split(':')

        game_number = int(game_number)

        samples = []
        sample_strings = game_data.split(';')
        for sample in sample_strings:
            cube_strings = sample.split(',')

            cubes = []
            for cube in cube_strings:
                colour_search = list(map(cube.find, COLOURS))
                colour_search = [1 if c > -1 else c for c in colour_search]
                colour = COLOURS[colour_search.index(1)]

                quantity = cube.replace(colour, '').strip()

                cubes.append(Cube(int(quantity), colour))
            
            samples.append(Sample(cubes))

        output.append(GameData(game_number, samples))

    return output



if __name__ == '__main__':
    print(get_vaule(input))