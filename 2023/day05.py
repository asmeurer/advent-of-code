test_input = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""

puzzle_input = open("day05_input").read().strip()

from dataclasses import dataclass, field

@dataclass
class MapRange:
    destination: int
    source: int
    length: int

@dataclass(unsafe_hash=True)
class Almanac:
    seeds: list[int] = field(default_factory=list)
    seed_to_soil: list[MapRange] = field(default_factory=list)
    soil_to_fertilizer: list[MapRange] = field(default_factory=list)
    fertilizer_to_water: list[MapRange] = field(default_factory=list)
    water_to_light: list[MapRange] = field(default_factory=list)
    light_to_temperature: list[MapRange] = field(default_factory=list)
    temperature_to_humidity: list[MapRange] = field(default_factory=list)
    humidity_to_location: list[MapRange] = field(default_factory=list)

def parse_input(input):
    almanac = Almanac()

    for line in input.splitlines():
        if not line.strip():
            pass
        elif line.startswith("seeds: "):
            almanac.seeds[:] = [int(s) for s in line.split(':')[1].split()]
        elif line.startswith("seed-to-soil map:"):
            current_map = almanac.seed_to_soil
        elif line.startswith("soil-to-fertilizer map:"):
            current_map = almanac.soil_to_fertilizer
        elif line.startswith("fertilizer-to-water map:"):
            current_map = almanac.fertilizer_to_water
        elif line.startswith("water-to-light map:"):
            current_map = almanac.water_to_light
        elif line.startswith("light-to-temperature map:"):
            current_map = almanac.light_to_temperature
        elif line.startswith("temperature-to-humidity map:"):
            current_map = almanac.temperature_to_humidity
        elif line.startswith("humidity-to-location map:"):
            current_map = almanac.humidity_to_location
        else:
            current_map.append(MapRange(*[int(s) for s in line.split()]))

    return almanac

def map_seed(seed, almanac):
    s = seed
    # print("seed number", s)
    for mapping in [almanac.seed_to_soil, almanac.soil_to_fertilizer, almanac.fertilizer_to_water, almanac.water_to_light, almanac.light_to_temperature, almanac.temperature_to_humidity, almanac.humidity_to_location]:
        for map_range in mapping:
            if map_range.source <= s < map_range.source + map_range.length:
                s = map_range.destination + (s - map_range.source)
                break
        # print(s)
    return s

def part1(almanac):
    mapped_seeds = [map_seed(seed, almanac) for seed in almanac.seeds]
    print(mapped_seeds)
    return min(mapped_seeds)

if __name__ == "__main__":
    print("Day 5")
    print("Part 1")
    print("Test input")
    test_almanac = parse_input(test_input)
    print(test_almanac)
    print(part1(test_almanac))
    print("Puzzle input")
    almanac = parse_input(puzzle_input)
    print(part1(almanac))
