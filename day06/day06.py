import threading
from typing import Optional
from collections import Counter


class LanternFish:
    def __init__(self, initial_value=8):
        self.timer = initial_value

    def decrement_timer(self) -> Optional['LanternFish']:
        if self.timer == 0:
            self.timer = 6
            return LanternFish()
        else:
            self.timer -= 1


def parse_input_obj(file_name: str) -> list[LanternFish]:
    with open(file_name, "r") as f:
        intitial_values = f.readline().split(',')
        return list(map(lambda x: LanternFish(int(x)), intitial_values))


def calculate_fishes_seq(file_name: str, days: int) -> int:
    fishes = parse_input_obj(file_name)
    for day in range(days):
        fish_to_add = []
        for fish in fishes:
            new_fish = fish.decrement_timer()
            if new_fish is not None:
                fish_to_add.append(new_fish)
        fishes.extend(fish_to_add)
    return len(fishes)


def calculate_fishes_parallel(fishes: list[LanternFish], days: int) -> int:
    pass


def parse_input_arr(file_name: str) -> list[int]:
    with open(file_name, "r") as f:
        intitial_values = f.readline().split(',')
        return list(map(int, intitial_values))


def calculate_fishes_fast(file_name: str, days: int) -> int:
    # population = {d: 0 for d in range(9)}  # day in cycle : number of fish
    fish_nums = parse_input_arr(file_name)
    population = Counter(fish_nums)
    for day in range(days):
        temp = population[0]
        for cycle in range(8):
            population[cycle] = population[cycle + 1]
        population[8] = temp
        population[6] = population[6] + temp
    total = 0
    for key, count in population.items():
        total += count
    return total


if __name__ == '__main__':
    # print(f'part one result: {calculate_fishes_seq("input-day6.txt", 80)}')
    print(f'part two result: {calculate_fishes_fast("input-day6.txt", 256)}')
