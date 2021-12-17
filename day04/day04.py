import numpy as np


def make_matrix(fd) -> np.array:
    new_matrix = np.empty([5, 5], dtype=int)
    row_num = 0

    line = fd.readline()
    if line == "":
        return None
    while line != "\n":
        j = 0
        # the last matrix in the file will be followed by a single line,
        # without a '\n' character
        if line == "":
            return new_matrix
        line = line.strip()
        entries = list(map(int, line.split()))
        for entry in entries:
            new_matrix[row_num][j] = entry
            j += 1
        row_num += 1
        line = fd.readline()

    return new_matrix


def parse_input(file_name: str) -> (list[int], list[np.array]):
    matrices = []

    with open(file_name, "r") as f:
        numbers = f.readline()
        numbers = list(map(int, numbers.split(",")))
        f.readline()
        matrix = make_matrix(f)
        while matrix is not None:
            matrices.append(matrix)
            matrix = make_matrix(f)

    return numbers, matrices


def mark_and_check(matrix, number) -> bool:
    row_index, col_index = np.where(matrix == number)

    if row_index.size == 0 or col_index.size == 0:
        return False
    matrix[row_index, col_index] = -1

    return matrix[row_index].sum() == -5 or matrix[:, col_index].sum() == -5


def sum_unchecked(matrix) -> int:
    total = 0

    for i, j in np.ndindex(matrix.shape):
        if matrix[i, j] != -1:
            total += matrix[i, j]

    return total


def calculate_score(matrix_sum, last) -> int:
    return matrix_sum * last


# PART ONE: finds the board that wins first and calculates its score
def part_one(input_file) -> int:
    numbers, matrices = parse_input(input_file)

    for number in numbers:
        for matrix in matrices:
            is_winner = mark_and_check(matrix, number)
            if is_winner:
                return calculate_score(sum_unchecked(matrix), number)


# PART TWO: finds the board that wins last
def part_two(input_file) -> int:
    numbers, matrices = parse_input(input_file)

    for number in numbers:
        winning_indices = []
        for index, matrix in enumerate(matrices):
            is_winner = mark_and_check(matrix, number)
            if is_winner and len(matrices) == 1:
                return calculate_score(sum_unchecked(matrix), number)
            elif is_winner:
                winning_indices.append(index)
        # removes items closer to the end of the list first to avoid shifting
        for index in sorted(winning_indices, reverse=True):
            matrices.pop(index)


if __name__ == '__main__':
    # print(part_one("input-day4.txt"))
    print(part_two("input-day4.txt"))

