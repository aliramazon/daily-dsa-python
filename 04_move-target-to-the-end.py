"""
Assignment: Move all occurrences of a given number to the end of a list.

Examples:
    Input: [1, 8, 8, 4, 11, 67, 8, 900, 12, 8, 13], 8
    Output: [1, 4, 11, 67, 900, 12, 13, 8, 8, 8, 8]

    Input: [5, 3, 5, 2, 1, 5, 7, 9], 5
    Output: [3, 2, 1, 7, 9, 5, 5, 5]
"""


def move_target_to_the_end_v1(numbers, target):
    slow = 0
    for idx, value in enumerate(numbers):
        if value != target:
            numbers[idx], numbers[slow] = numbers[slow], numbers[idx]
            slow += 1
    return numbers


def move_target_to_the_end_v2(numbers, target):
    insert_pos = 0

    for value in numbers:
        if value != target:
            numbers[insert_pos] = value
            insert_pos += 1

    while insert_pos < len(numbers):
        numbers[insert_pos] = target
        insert_pos += 1
    return numbers


print(
    move_target_to_the_end_v2([1, 8, 4, 11, 67, 8, 900, 12, 8, 13], 8)
    == [1, 4, 11, 67, 900, 12, 13, 8, 8, 8]
)
print(
    move_target_to_the_end_v2([5, 3, 5, 2, 1, 5, 7, 9], 5) == [3, 2, 1, 7, 9, 5, 5, 5]
)
print(move_target_to_the_end_v2([], 1) == [])
print(move_target_to_the_end_v2([1, 1, 1, 1], 1) == [1, 1, 1, 1])
print(move_target_to_the_end_v2([10, 20, 30], 5) == [10, 20, 30])
