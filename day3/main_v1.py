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

def find_highiest_pairing(data: list[LiteralString] | list[str]) -> int:
    """
    Approach:
    - Split the numbers into  individual characters while eliminating duplicates: list(set(list(STRING)))
    - Create a list of every 2-character permutation possible
    - Find the highest number
    """
    total = 0
    pairing_size = 2

    for number_string in data:
        number_parts = list(set(list(number_string.strip())))
        combinations = itertools.combinations(number_parts, pairing_size) # [(1, 1), (1, 2), ...]
        combinations_as_integers = [int(''.join(c)) for c in combinations]
        total += max(combinations_as_integers)

        print(number_string, max(combinations_as_integers))

    return total

if __name__ == "__main__":
    print("Advent of Code 2025 - Day 3")
    data = get_data(use_example=True)
    highest_pairing = find_highiest_pairing(data)
    print("Highest Pairing: ", highest_pairing)