import copy
import numpy as np

# PART ONE
# with open("input-day3.txt", "r") as nums:
#     values_list = []
#     gamma = []
#     epsilon = []
#
#     for line in nums.readlines():
#         line = line.strip()
#         values_list.append(np.asarray(list(map(int, list(line)))))
#     num_lines = len(values_list)
#
#     values_matrix = np.asarray(values_list)
#     values_matrix = values_matrix.transpose()
#
#     for row in values_matrix:
#         count = np.sum(row)
#         if count < num_lines / 2:
#             gamma.append("1")
#             epsilon.append("0")
#         else:
#             gamma.append("0")
#             epsilon.append("1")
#
#     gamma = "".join(gamma)
#     epsilon = "".join(epsilon)
#
#     power = int(gamma, 2) * int(epsilon, 2)
#
#     print(f"power consumption: {power}")

# PART TWO
with open("input-day3.txt", "r") as nums:
    values_list = []
    oxygen_rating = 0
    scrubber_rating = 0
    # product will be zero if one of these is not set

    for line in nums.readlines():
        line = line.strip()
        values_list.append(np.asarray(list(map(int, list(line)))))
    num_lines = len(values_list)

    values_matrix = np.asarray(values_list)
    matrix1 = values_matrix.transpose()
    matrix2 = copy.deepcopy(matrix1)

    # handle most and least common separately
    # iterate over the first row, find the most common
    # then iterate over the first row and delete any columns
    # that do not begin with that number
    num_rows = matrix1.shape[0]
    num_cols = matrix1.shape[1]

    row_index = 0
    while num_cols > 1:
        row = matrix1[row_index, :]
        count = np.sum(row)
        eliminate = 0 if count >= num_cols / 2 else 1
        indices = []
        for index, entry in np.ndenumerate(row):
            if entry == eliminate:
                indices.append(index)
        matrix1 = np.delete(matrix1, indices, 1)
        row_index += 1
        num_cols = matrix1.shape[1]
    oxygen_rating = matrix1[:, 0]
    oxygen_rating = oxygen_rating.tolist()
    oxygen_rating = "".join(list(map(str, oxygen_rating)))
    oxygen_rating = int(oxygen_rating, 2)

    num_rows = matrix2.shape[0]
    num_cols = matrix2.shape[1]

    row_index = 0
    while num_cols > 1:
        row = matrix2[row_index, :]
        count = np.sum(row)
        eliminate = 1 if count >= num_cols / 2 else 0
        indices = []
        for index, entry in np.ndenumerate(row):
            if entry == eliminate:
                indices.append(index)
        matrix2 = np.delete(matrix2, indices, 1)
        row_index += 1
        num_cols = matrix2.shape[1]
    scrubber_rating = matrix2[:, 0]
    scrubber_rating = scrubber_rating.tolist()
    scrubber_rating = "".join(list(map(str, scrubber_rating)))
    scrubber_rating = int(scrubber_rating, 2)

    print(f"life support rating: {oxygen_rating * scrubber_rating}")

