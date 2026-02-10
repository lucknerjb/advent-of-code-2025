import itertools

from typing import LiteralString


def get_data(use_example: bool=False) -> list[LiteralString] | list[str]:
    if use_example:
        inputs = """3-5
10-14
16-20
12-18

1
5
8
11
17
32""".split("\n\n")
    else:
        with open("./data.txt") as f:
            inputs = f.read().strip().split("\n\n")

    return inputs

def get_fresh_ingredient_count(data: list[LiteralString] | list[str], part_1_or_2: int=1) -> int:
    """
    Approach:
    - Build a list containing all the IDs from the valid ranges
    - Build a list of the IDs we are looking to check
    - Count the resulting intersection of these 2 lists
    """
    # ranges = []
    # # Build ranges
    # for row in data[0].splitlines():
    #     row_parts = row.split("-")
    #     ranges = list(set(ranges + [number for number in range(int(row_parts[0]), int(row_parts[1]) + 1)]))

    # # Build list of ingredient IDs
    # ingredient_ids = [int(id_string) for id_string in data[1].splitlines()]

    # return len([x for x in ingredient_ids if x in ranges])

    ranges = []
    for row in data[0].splitlines():
        row_parts = row.split("-")
        ranges.append({"start": int(row_parts[0]), "end": int(row_parts[1])})
    print(ranges)

    count = 0
    ingredient_ids = [int(id_string) for id_string in data[1].splitlines()]

    for ingredient_id in ingredient_ids:
        for fresh_range in ranges:
            if ingredient_id >= fresh_range["start"] and ingredient_id <= fresh_range["end"]:
                count += 1
                break

    return count
    

if __name__ == "__main__":
    print("Advent of Code 2025 - Day 5")
    data = get_data(use_example=False)
    count = get_fresh_ingredient_count(data, part_1_or_2=2)
    print("Fresh Ingredients: ", count)
