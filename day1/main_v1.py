def get_operations(use_example=False):
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

def perform_rotations(inputs, use_example=False, print_rotations=False):
    dial_number = 50
    number_of_zeros = 0
    for operation in inputs:
        operation = operation.strip()
        turn = operation[0]
        distance = int(operation[1:])

        # # Grab the remainder of the distance divided by 99, unless the distance is exactly 99, in which case we want to use 99
        # distance = distance_int % 100 if distance_int != 100 else 100

        # Perform a crude turn of the dial, and then adjust the dial number to be between 0 and 99
        # if turn == "L":
        #     dial_number -= distance
        # else:
        #     dial_number += distance

        if turn == "L":
            distance *= -1

        dial_number = _perform_single_rotation(dial_number, distance)

        # # We went past 0 to the left and so we can simply subtract that number from 100
        # if dial_number < 1:
        #     dial_number = 100 + dial_number

        # # We went past 99 to the right and so we can simply subtract 100 from the number
        # if dial_number > 100:
        #     dial_number = dial_number - 100

        # We landed directly on 100, which means 0 as that is the same as 99 + 1
        # if dial_number == 100:
        #     dial_number = 0

        
        number_of_zeros += 1 if dial_number == 0 else 0

        if print_rotations:
            print(f"Turn: {turn}, Distance: {distance}, Dial Number: {dial_number}")
    
    return number_of_zeros


def _perform_single_rotation(start, ticks):
    return (start + ticks) % 100

    # Grab the remainder of the distance divided by 99, unless the distance is exactly 99, in which case we want to use 99
    distance = ticks % 100 if ticks != 100 else 100

    dial_number = start + distance

     # We went past 0 to the left and so we can simply subtract that number from 100
    if dial_number < 1:
        dial_number = 100 + dial_number

    # We went past 99 to the right and so we can simply subtract 100 from the number
    if dial_number > 100:
        dial_number = dial_number - 100

    return dial_number


if __name__ == "__main__":
    print("Advent of Code 2025 - Day 1")
    operations = get_operations(use_example=False)
    print("Times landed on 0:", perform_rotations(inputs=operations, print_rotations=True))