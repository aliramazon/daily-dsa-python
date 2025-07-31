"""
Move all zeros to the end of a list while maintaining the order of the other elements.

Given a list of integers, write a function to move all 0's to the end of it
while maintaining the relative order of the non-zero elements.

Constraints:
- The operation must be done in-place, without creating a copy of the list.
- Minimize the total number of operations.

Examples:
arr = [0, 1, 0, 3, 12]
output: [1, 3, 12, 0, 0]

arr = [1, 2, 0, 4, 3, 0, 5, 0]
output: [1, 2, 4, 3, 5, 0, 0, 0]

arr = [1]
output: [1]

arr = [0, 0, 1]
output: [1, 0, 0]
"""


def move_zeros_to_the_end_v1(numbers):
    zero_pos = 0

    for idx, value in enumerate(numbers):
        if value != 0:
            numbers[zero_pos], numbers[idx] = numbers[idx], numbers[zero_pos]
            zero_pos += 1
    return numbers


def move_zeros_to_the_end_v2(numbers):
    insert_pos = 0

    for value in numbers:
        if value != 0:
            numbers[insert_pos] = value
            insert_pos += 1

    while insert_pos < len(numbers):
        numbers[insert_pos] = 0
        insert_pos += 1

    return numbers


print(move_zeros_to_the_end_v1([1, 2, 0, 4, 3, 0, 5, 0]))  # [1, 2, 4, 3, 5, 0, 0, 0]
print(move_zeros_to_the_end_v1([0, 1, 0, 3, 12]))  # [1, 3, 12, 0, 0]
print(move_zeros_to_the_end_v1([1]))  # [1]
print(move_zeros_to_the_end_v1([0, 0, 1]))  # [1, 0, 0]
print(move_zeros_to_the_end_v1([0, 0, 0]))  # [0, 0, 0]
print(move_zeros_to_the_end_v1([4, 5, 6]))  # [4, 5, 6]
print(move_zeros_to_the_end_v1([]))  # []


print(move_zeros_to_the_end_v2([1, 2, 0, 4, 3, 0, 5, 0]))  # [1, 2, 4, 3, 5, 0, 0, 0]
print(move_zeros_to_the_end_v2([0, 1, 0, 3, 12]))  # [1, 3, 12, 0, 0]
print(move_zeros_to_the_end_v2([1]))  # [1]
print(move_zeros_to_the_end_v2([0, 0, 1]))  # [1, 0, 0]
print(move_zeros_to_the_end_v2([0, 0, 0]))  # [0, 0, 0]
print(move_zeros_to_the_end_v2([4, 5, 6]))  # [4, 5, 6]
print(move_zeros_to_the_end_v2([]))  # []
