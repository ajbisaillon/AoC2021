# PART ONE
with open("input-day1.txt", "r") as nums:
    counter = 0
    previous = None
    for line in nums.readlines():
        num = int(line)
        if previous and num > previous:
            counter += 1
        previous = num
    print(f"part one output: {counter}")


# PART TWO
with open("input-day1.txt", "r") as nums:
    counter = 0
    window = []

    for line in nums.readlines():
        num = int(line)

        if len(window) < 4:
            window.append(num)
            if len(window) == 4:
                sum1 = sum(window[0:3])
                sum2 = sum(window[1:4])
                if sum2 > sum1:
                    counter += 1
        else:
            sum1 = sum(window[0:3])
            sum2 = sum(window[1:4])
            if sum2 > sum1:
                counter += 1
            window.pop(0)
            window.append(num)

    print(f"part two output: {counter}")

