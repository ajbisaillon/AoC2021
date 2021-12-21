import numpy as np


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_horizontal(self, other: "Point") -> bool:
        return self.y == other.y

    def is_vertical(self, other: "Point") -> bool:
        return self.x == other.x

    def __eq__(self, other: "Point") -> bool:
        return self.x == other.x and self.y == other.y


class Grid:  # ocean floor
    def __init__(self, num_rows, num_cols):
        self.grid = np.zeros((num_rows, num_cols))

    def mark_hpath(self, point1: Point, point2: Point):
        start = min(point1.x, point2.x)
        end = max(point1.x, point2.x)
        i = point1.y

        for j in range(start, end+1):
            self.grid[i, j] = self.grid[i, j] + 1

    def mark_vpath(self, point1: Point, point2: Point):
        start = min(point1.y, point2.y)
        end = max(point1.y, point2.y)
        j = point1.x

        for i in range(start, end + 1):
            self.grid[i, j] = self.grid[i, j] + 1

    def mark_dpath(self, point1: Point, point2: Point):
        # find point with minimum y-value - start at that point
        start_point = min(point1, point2, key=lambda p: p.y)

        if start_point == point1 and point2.x < point1.x:
            direction = -1
            end = point2.y
        elif start_point == point2 and point1.x < point2.x:
            direction = -1
            end = point1.y
        elif start_point == point1 and point1.x < point2.x:
            direction = 1
            end = point2.y
        else:  # start_point == point2 and point2.x < point1.x
            direction = 1
            end = point1.y

        start = start_point.y
        j = start_point.x

        for i in range(start, end + 1):
            self.grid[i, j] = self.grid[i, j] + 1
            j += direction

    def mark_path(self, point1: Point, point2: Point):
        if point1.is_horizontal(point2):
            self.mark_hpath(point1, point2)
        elif point1.is_vertical(point2):
            self.mark_vpath(point1, point2)
        else:
            self.mark_dpath(point1, point2)

    def count_overlaps(self, num: int) -> int:
        overlap_indices = np.argwhere(self.grid >= num)
        return overlap_indices.shape[0]


def parse_input(file_name: str) -> list[(Point, Point)]:
    points_list = []
    separator = " -> "
    with open(file_name, "r") as f:
        for line in f.readlines():
            points = line.split(separator)
            point1 = list(map(int, points[0].split(",")))
            point2 = list(map(int, points[1].split(",")))
            points_list.append((Point(point1[0], point1[1]), Point(point2[0], point2[1])))
    return points_list


if __name__ == '__main__':
    points = parse_input("input-day5.txt")
    ocean_grid = Grid(1000, 1000)
    for point in points:
        ocean_grid.mark_path(point[0], point[1])
    print(ocean_grid.count_overlaps(2))

    # add optional disable for diagonal lines
