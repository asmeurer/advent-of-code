test_input = """
Time:      7  15   30
Distance:  9  40  200
""".strip()

puzzle_input = open("day06_input").read().strip()

from sympy import symbols, Integers, reduce_inequalities, prod

def parse_input(input):
    times = map(int, input.split("\n")[0].split(':')[1].split())
    distances = map(int, input.split("\n")[1].split(':')[1].split())
    return list(zip(times, distances))


def race_distance(held_time, time):
    rate = held_time
    remaining_time = time - held_time
    return rate * remaining_time

def solve_race(time, distance):
    x = symbols('x')
    sol_set = reduce_inequalities(race_distance(x, time) > distance).as_set()
    return set(sol_set.intersection(Integers))

def part1(races):
    solutions = []
    for time, distance in races:
        sol = solve_race(time, distance)
        print(len(sol), sol)
        solutions.append(sol)

    return prod(map(len, solutions))

if __name__ == "__main__":
    print("Day 6")
    print("Part 1")
    print("Test input")
    test_races = parse_input(test_input)
    print(part1(test_races))
    print("Puzzle input")
    races = parse_input(puzzle_input)
    print(part1(races))
