"""Day 02: Dive!"""


def part_one(input: list[str]) -> int:
    horizontal_pos: int = 0
    depth: int = 0

    for command in input:
        instruction, value = command.split()
        if instruction == "down":
            depth += int(value)
        elif instruction == "up":
            depth -= int(value)
        else:
            horizontal_pos += int(value)

    return horizontal_pos * depth


def part_two(input: list[str]) -> int:
    horizontal_pos: int = 0
    depth: int = 0
    aim: int = 0

    for command in input:
        instruction, value = command.split()
        if instruction == "down":
            aim += int(value)
        elif instruction == "up":
            aim -= int(value)
        else:
            horizontal_pos += int(value)
            depth += aim * int(value)

    return horizontal_pos * depth


if __name__ == "__main__":
    with open("input/day_02.txt", "r") as f:
        commands: list[str] = [line.strip() for line in f]

    print(f"Part one: {part_one(commands)}")
    print(f"Part two: {part_two(commands)}")
