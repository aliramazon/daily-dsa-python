"""
Create a function `rotate_right_till_zero` that takes an integer array containing one 0
and rotates the array to the right (clockwise) so that the 0 ends up at the last position.

Examples:

Input:  [0, 1, 2, 3]
Output: [1, 2, 3, 0]          # Rotated right 1 step

Input:  [1, 0, 2, 3]
Output: [2, 3, 1, 0]          # Rotated right 2 steps

Input:  [1, 0, 2, 3, 4, 5, 6]
Output: [2, 3, 4, 5, 6, 1, 0] # Rotated right 2 steps

Input:  [1, 8, 2, 3, 4, 0, 7]
Output: [7, 1, 8, 2, 3, 4, 0] # Rotated right 1 step

Input:  [1, 8, 2, 3, 0, 5, 6]
Output: [5, 6, 1, 8, 2, 3, 0] # Rotated right 2 steps

Input:  [1, 8, 2, 3, 4, 5, 0]
Output: [1, 8, 2, 3, 4, 5, 0] # Already has 0 at end → No rotation
"""


def rotate_right_till_zero_v1(numbers):
    while numbers[-1] != 0:
        numbers.insert(0, numbers.pop())
    return numbers


from collections import deque


def rotate_right_till_zero_v2(numbers):
    dq = deque(numbers)

    while dq[-1] != 0:
        dq.appendleft(dq.pop())
    return list(dq)


def rotate_right_till_zero_v3(numbers):
    result = []
    zero_pos = 0

    for idx, value in enumerate(numbers):
        if value == 0:
            zero_pos = idx
        result.append(0)

    offset = len(numbers) - 1 - zero_pos

    for idx, value in enumerate(numbers):
        new_pos = (idx + offset) % len(numbers)
        result[new_pos] = value
    return result


print(rotate_right_till_zero_v3([0, 1, 2, 3]))  # [1, 2, 3, 0]
print(rotate_right_till_zero_v3([1, 0, 2, 3]))  # [2, 3, 1, 0]
print(rotate_right_till_zero_v3([1, 0, 2, 3, 4, 5, 6]))  # [2, 3, 4, 5, 6, 1, 0]
print(rotate_right_till_zero_v3([1, 8, 2, 3, 4, 0, 7]))  # [7, 1, 8, 2, 3, 4, 0]
print(rotate_right_till_zero_v3([1, 8, 2, 3, 0, 5, 6]))  # [5, 6, 1, 8, 2, 3, 0]
print(rotate_right_till_zero_v3([1, 8, 2, 3, 4, 5, 0]))  # [1, 8, 2, 3, 4, 5, 0]
