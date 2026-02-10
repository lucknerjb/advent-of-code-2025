from typing import LiteralString


def get_data(use_example: bool=False) -> list[LiteralString] | list[str]:
    if use_example:
        inputs = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124""".split(',')
    else:
        with open("./data.txt") as f:
            inputs = f.read().strip().split(',')

    return inputs

def find_invalid_ids(data: list[LiteralString] | list[str], part_1_or_2: int=1) -> list[int]:
    invalid_ids = []
    for ids_range in data:
        parts = ids_range.split('-')
        start = int(parts[0])
        end = int(parts[1])

        # Loop over all the numbers in the range and if we have an even number of integers in the current iteration,
        # check to see if the first half equals the second half
        for i in range(start, end + 1):
            number_as_string = str(i)
            length = len(str(i))

            # Skip processing anything if we don't have at least 2 numbers
            if length < 2:
                continue
            
            # Part 1
            if part_1_or_2 == 1:
                if length % 2 != 0:
                    continue

                midpoint = int(length / 2)
                left_half = number_as_string[midpoint:]
                right_half = number_as_string[:midpoint]

                if left_half == right_half:
                    invalid_ids.append(i)
            
                continue

            # Part 2
            # Add numbers where the sequence of numbers occurs at least twice. This will include
            # numbers that contain only a single type of digit - ie 999 or group - ie 123123

            # First, check to see if all the characters in the number are all the same
            unique_number_parts = set(list(number_as_string))
            if len(unique_number_parts) == 1:
                invalid_ids.append(i)
                continue

            """
            Second, check through each integer group in the number to see if we have repetition. Process:
            - Determine the length of the number
            - Create groups from its parts (ie: 123123 => 12, 123, 1231, 12312, 123123)
            - We can split the string on the groups and if we have a list full of empty values, we have repetition
            - If we have an even-length string, we'll stop at the midpoint
            - If we have an odd-length string, we'll stop at the midpoint of length - 1
            """
            # YUCK
            max_index = length / 2 if length % 2 == 0 else (length - 1) / 2

            max_index = int(length / 2)
            if length % 2 != 0:
                max_index = int((length - 1) / 2)

            # We can skip index 0, which would yield an empty string
            # We can skip index 1 since that's covered by the case above where all numbers are a single digit repeated
            start_index = 2
            groups = [number_as_string[:index] for index in range(start_index, max_index + 1)]

            for group in groups:
                # Loop through all the groups and see if we have
                number_split_by_groups = number_as_string.split(group)
                if all([not s for s in number_split_by_groups]):
                    invalid_ids.append(i)
                    break


    return invalid_ids


if __name__ == "__main__":
    print("Advent of Code 2025 - Day 2")
    data = get_data(use_example=False)
    invalid_ids = find_invalid_ids(data, part_1_or_2=2)
    print(invalid_ids)
    print("Sum of invalid IDs: ", sum(invalid_ids))
    # print("Times landed on 0:", perform_rotations(inputs=operations, print_rotations=True))