"""Day 01: Sonar Sweep"""


def part_one(input: list[int]) -> int:
    return sum(1 for i in range(1, len(input)) if input[i] > input[i - 1])


def part_two(input: list[int]) -> int:
    return sum(1 for i in range(3, len(input)) if input[i] > input[i - 3])


if __name__ == "__main__":
    with open("input/day_01.txt", "r") as f:
        depths: list[int] = [int(line.strip()) for line in f]

    print(f"Part one: {part_one(depths)}")
    print(f"Part two: {part_two(depths)}")
