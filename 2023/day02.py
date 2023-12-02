test_input = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
""".strip()

puzzle_input = open("day02_input").read().strip()

def parse_input(input):
    for line in input.splitlines():
        game_id, game = line.split(":")
        rounds = game.split(";")
        rounds = [round.split(", ") for round in rounds]
        rounds = [[cubes.strip().split(" ") for cubes in round] for round in rounds]
        rounds = [{cubes[1]: int(cubes[0]) for cubes in round} for round in rounds]
        yield int(game_id.split()[1]), rounds

bag = {"red": 12, "green": 13, "blue": 14}

def part_1(games):
    good_games = []
    bad = False
    for game_id, rounds in games:
        for round in rounds:
            for color, n in round.items():
                if n > bag[color]:
                    bad = True
                    break
            if bad:
                break
        if not bad:
            good_games.append(game_id)
        bad = False
    print(good_games)
    return sum(good_games)

if __name__ == "__main__":
    print("Day 2")
    print("Part 1")
    print("Test input")
    test_games = list(parse_input(test_input))
    games = list(parse_input(puzzle_input))
    print(test_games)
    print(part_1(test_games))
    print("Puzzle input")
    print(part_1(games))
