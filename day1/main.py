from typing import LiteralString


def get_operations(use_example: bool=False) -> list[LiteralString] | list[str]:
    if use_example:
        inputs = """
            L168
            L30
            R48
            L5
            R60
            L55
            L1
            L99
            R14
            L82
        """.strip().splitlines()
    else:
        with open("./data.txt") as f:
            inputs = f.read().strip().splitlines()

    return inputs

def perform_rotations(inputs: list[LiteralString] | list[str], print_rotations: bool=False) -> int:
    dial_number = 50
    number_of_zeros = 0
    for operation in inputs:
        operation = operation.strip()
        turn = operation[0]
        distance = int(operation[1:])

        if turn == "L":
            distance *= -1

        dial_number = _perform_single_rotation(dial_number, distance)
        number_of_zeros += 1 if dial_number == 0 else 0

        if print_rotations:
            print(f"Turn: {turn}, Distance: {distance}, Dial Number: {dial_number}")
    
    return number_of_zeros


def _perform_single_rotation(start: int, ticks: int) -> int:
    return (start + ticks) % 100


if __name__ == "__main__":
    print("Advent of Code 2025 - Day 1")
    operations = get_operations(use_example=False)
    print("Times landed on 0:", perform_rotations(inputs=operations, print_rotations=True))