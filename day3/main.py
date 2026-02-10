import itertools

from typing import LiteralString


def get_data(use_example: bool=False) -> list[LiteralString] | list[str]:
    if use_example:
        inputs = """987654321111111
            811111111111119
            234234234234278
            818181911112111""".splitlines()
    else:
        with open("./data.txt") as f:
            inputs = f.read().strip().splitlines()

    return inputs

def get_max_voltage(data: list[LiteralString] | list[str], part_1_or_2: int=1) -> int:
    """
    Approach:
    - Split the numbers into  individual characters while eliminating duplicates: list(set(list(STRING)))
    - Create a list of every 2-character permutation possible
        - Note, permutations can only be made with numbers to the right of the current number
    - Find the highest number
    """
    total = 0

    for number_string in data:
        number_string = number_string.strip()
        all_numbers = []
        length = len(number_string)

        if part_1_or_2 == 1:
            for first_character_index, _ in enumerate(number_string.strip()):
                for second_character_index in range(first_character_index + 1, length):
                    first_number = number_string[first_character_index]
                    second_number = number_string[second_character_index]
                    number = int(''.join([first_number, second_number]))
                    all_numbers.append(number)
            total += max(all_numbers)
            continue

        # Part 2a
        # number_parts = list(number_string)
        # combinations = itertools.combinations(number_parts, 12)
        # combination_numbers = [int(''.join(c)) for c in combinations]
        # total += max(combination_numbers)

        # Part 2b - can't re-order
        # number_parts = [int(number) for number in list(number_string)]
        # number_parts.sort(reverse=True)
        
        # final_number = int(''.join([str(number) for number in number_parts[0:12]]))
        # print(number_string, final_number)
        # total += int(''.join([str(number) for number in number_parts[0:12]]))

        # Part 2
        picked = []
        numbers_to_drop = length - 12
        for digit in number_string:
            while numbers_to_drop and picked and picked[-1] < digit:
                picked.pop()
                numbers_to_drop -= 1

            picked.append(digit)
        total += int(''.join(picked[0:12]))
        print(''.join(picked[0:12]))

    return total

if __name__ == "__main__":
    print("Advent of Code 2025 - Day 3")
    data = get_data(use_example=False)
    max_voltage = get_max_voltage(data, part_1_or_2=2)
    print("Highest Pairing: ", max_voltage)