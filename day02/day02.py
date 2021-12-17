# PART ONE
# with open("input-day2.txt", "r") as controls:
#     vertical = 0  # depth
#     horizontal = 0
#
#     for line in controls.readlines():
#         [direction, amount] = line.split()  # destructuring
#
#         amount = int(amount)
#
#         if direction == "forward":
#             horizontal += amount
#         elif direction == "up":
#             vertical -= amount
#         elif direction == "down":
#             vertical += amount
#         else:
#             raise Exception("Invalid direction")
#
#     print(f"position: {horizontal * vertical}")

# PART TWO
with open("input-day2.txt", "r") as controls:
    vertical = 0  # depth
    horizontal = 0
    aim = 0

    for line in controls.readlines():
        [direction, amount] = line.split()  # destructuring

        amount = int(amount)

        if direction == "forward":
            horizontal += amount
            vertical += aim * amount
        elif direction == "up":
            aim -= amount
        elif direction == "down":
            aim += amount
        else:
            raise Exception("Invalid direction")

    print(f"position: {horizontal * vertical}")