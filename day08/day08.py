def parse_input(file_name: str) -> list[(list[str], list[str])]:
    result = []
    with open(file_name, "r") as f:
        for line in f.readlines():
            scrambled_segments = []
            right = []
            parts = line.strip().split(" | ")
            for part in parts[0].split(" "):
                scrambled_segments.append(part)
            for part in parts[1].split(" "):
                right.append(part)
            result.append((scrambled_segments, right))
    return result


def part_one(file_name: str) -> int:
    entries = parse_input(file_name)
    count = 0
    for _, right in entries:
        for sequence in right:
            if len(sequence) in [2, 3, 4, 7]:
                count += 1
    return count


def get_overlaps(segments1: set[str], segments2: set[str]) -> int:
    count = 0
    for seg in segments2:
        if seg in segments1:
            count += 1
    return count


def create_mapping(scrambled_segments: list[str]) -> list[set[str]]:
    segment_map = [set() for _ in range(10)]
    segment_map[1] = set(list(filter(lambda x: len(x) == 2, scrambled_segments))[0])
    segment_map[4] = set(list(filter(lambda x: len(x) == 4, scrambled_segments))[0])
    segment_map[7] = set(list(filter(lambda x: len(x) == 3, scrambled_segments))[0])
    segment_map[8] = set(list(filter(lambda x: len(x) == 7, scrambled_segments))[0])
    five_segment_digits = list(filter(lambda x: len(x) == 5, scrambled_segments))
    for digit in five_segment_digits:
        segments = set(digit)
        if get_overlaps(segment_map[1], segments) == 2:
            segment_map[3] = segments
        elif get_overlaps(segment_map[4], segments) == 3:
            segment_map[5] = segments
        else:
            segment_map[2] = segments
    six_segment_digits = list(filter(lambda x: len(x) == 6, scrambled_segments))
    for digit in six_segment_digits:
        segments = set(digit)
        if get_overlaps(segment_map[1], segments) == 1:
            segment_map[6] = segments
        elif get_overlaps(segment_map[3], segments) == 5:
            segment_map[9] = segments
        else:
            segment_map[0] = segments
    return segment_map


def decode_number(mapping: list[set[str]], encoded_digits: list[str]) -> int:
    number_string = ""
    for digit in encoded_digits:
        index = mapping.index(set(digit))
        number_string += str(index)
    return int(number_string)


def part_two(file_name: str) -> int:
    entries = parse_input(file_name)
    total = 0
    for left, right in entries:
        segment_map = create_mapping(left)
        total += decode_number(segment_map, right)
    return total


if __name__ == '__main__':
    print(part_one("input-day8.txt"))
    print(part_two("input-day8.txt"))
