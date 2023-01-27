"""Day 03: Binary Diagnostic"""


def part_one(input: list[str]) -> int:
    gamma_rate = ""
    epsilon_rate = ""

    for pos in range(len(input[0])):
        zero_count: int = 0
        one_count: int = 0

        for bin_code in input:
            if bin_code[pos] == "0":
                zero_count += 1
            else:
                one_count += 1

        if zero_count > one_count:
            gamma_rate += "1"
            epsilon_rate += "0"
        else:
            gamma_rate += "0"
            epsilon_rate += "1"

    power_consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)
    return power_consumption


def part_two(input: list[str]) -> int:
    life_support_rating = int(_oxygen_generator_rating(input), 2) * int(
        _co2_scrubber_rating(input), 2
    )
    return life_support_rating


def _oxygen_generator_rating(input: list[str]) -> str:
    bit_count: int = len(input[0])
    for pos in range(bit_count):
        if len(input) > 1:
            zero_count = 0
            one_count = 0
            for bin_code in input:
                if bin_code[pos] == "0":
                    zero_count += 1
                else:
                    one_count += 1

            if one_count >= zero_count:
                input = [bin_code for bin_code in input if bin_code[pos] == "1"]
            else:
                input = [bin_code for bin_code in input if bin_code[pos] == "0"]
    return input[0]


def _co2_scrubber_rating(input: list[str]) -> str:
    bit_count: int = len(input[0])
    for pos in range(bit_count):
        if len(input) > 1:
            zero_count = 0
            one_count = 0
            for bin_code in input:
                if bin_code[pos] == "0":
                    zero_count += 1
                else:
                    one_count += 1

            if one_count < zero_count:
                input = [bin_code for bin_code in input if bin_code[pos] == "1"]
            else:
                input = [bin_code for bin_code in input if bin_code[pos] == "0"]
    return input[0]


if __name__ == "__main__":
    with open("input/day_03.txt", "r") as f:
        diagnostic_report: list[str] = [line.strip() for line in f]

    print(f"Part one: {part_one(diagnostic_report)}")
    print(f"Part two: {part_two(diagnostic_report)}")
