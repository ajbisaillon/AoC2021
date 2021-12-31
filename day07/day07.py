from typing import Callable


def parse_input(file_name: str) -> list[int]:
    with open(file_name, "r") as f:
        line = f.readline()
        nums = list(map(int, line.split(",")))
        return nums


def calculate_cost_constant(difference: int) -> int:
    return difference


def calculate_cost_variable(difference: int) -> int:
    return sum(range(1, difference + 1))


def calculate_total_cost(nums: list[int], destination: int, cost_func: Callable[[int], int]) -> int:
    acc = 0
    for num in nums:
        distance = abs(num - destination)
        acc += cost_func(distance)
    return acc


def part_one(file_name: str) -> int:
    nums = parse_input(file_name)
    max_position = max(nums)
    min_fuel = float("inf")
    for n in range(max_position + 1):
        fuel_cost = calculate_total_cost(nums, n, calculate_cost_constant)
        if fuel_cost < min_fuel:
            min_fuel = fuel_cost
    return min_fuel


def part_two(file_name: str) -> int:
    nums = parse_input(file_name)
    max_position = max(nums)
    min_fuel = float("inf")
    for n in range(max_position + 1):
        fuel_cost = calculate_total_cost(nums, n, calculate_cost_variable)
        if fuel_cost < min_fuel:
            min_fuel = fuel_cost
    return min_fuel


if __name__ == '__main__':
    # print(part_one("input-day7.txt"))
    print(part_two("input-day7.txt"))

