import itertools

from typing import LiteralString


def get_data(use_example: bool=False) -> list[LiteralString] | list[str]:
    if use_example:
        inputs = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.""".splitlines()
    else:
        with open("./data.txt") as f:
            inputs = f.read().strip().splitlines()

    return inputs

def _get_adjacent_cell_coordinates(row: int, col: int) -> list[tuple]:
    """
    Adjacent cell grid:

    YYY
    YXY
    YYY
    """
    top_left = (row - 1, col - 1,)
    top = (row - 1, col,)
    top_right = (row - 1, col + 1,)
    right = (row, col + 1,)
    bottom_right = (row + 1, col + 1,)
    bottom = (row + 1, col,)
    bottom_left = (row + 1, col - 1,)
    left = (row, col - 1,)

    return [
        top_left,
        top,
        top_right,
        right,
        bottom_right,
        bottom,
        bottom_left,
        left
    ]

def _get_roll_count_in_adjacent_cells(grid: list[list[str]], coordinates: list[tuple], rows: int, cols: int) -> int:
    """Returns the number of rolls found in adjacent cells"""
    count = 0

    for coordinate in coordinates:
        x, y = coordinate
        valid_row = 0 <= x and x < rows
        valid_column = 0 <= y and y < cols
    
        if valid_row and valid_column:
            print(x, y, grid[x][y])
            count += 1 if grid[x][y] == "@" else 0

    return count

# def _remove_from_grid(grid: list[list[str], row: int, col: int) -> None:
#     grid[x][y] = 'X'  # Mark roll as removed
#     return grid

def get_accessible_rolls(data: list[LiteralString] | list[str], part_1_or_2: int=1) -> int:
    """
    Approach:
    - Create a grid of the input data
    - Determine the coordinates of the 8 adjacent cells for each cell
    - Iterate through all the cells and if there is a roll there, check the count of rolls in the 8 adjacent cells
    - If the cell adjacent cell coordinate is not valid, skip over it quietly
    """
    grid = [list(line.strip()) for line in data]
    grid_row_count = len(grid)
    grid_column_count = len(grid[0])
    count = 0
    
    while True:
        removed = False
        for row_index, row in enumerate(grid):
            print("==================================== NEW RUN ====================================")
            for column_index, column in enumerate(row):
                # Skip if we don't even have a roll in this cell
                if column != "@":
                    continue

                print('==========================')
                print(row_index, column_index, column)
                coordinates = _get_adjacent_cell_coordinates(row_index, column_index)
                print(row_index, column_index, coordinates)
                roll_count = _get_roll_count_in_adjacent_cells(grid, coordinates, grid_row_count, grid_column_count)
                print(roll_count)
                if roll_count < 4:
                    count += 1
                    
                    # Remove from grid
                    grid[row_index][column_index] = 'X'
                    removed = True
        if part_1_or_2 == 1 or not removed:
            break
    return count

if __name__ == "__main__":
    print("Advent of Code 2025 - Day 4")
    data = get_data(use_example=False)
    accessible_rolls = get_accessible_rolls(data, part_1_or_2=2)
    print("Highest Pairing: ", accessible_rolls)