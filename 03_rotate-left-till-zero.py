"""
Create a function that takes an integer array containing one 0 and rotates the array counterclockwise so that the 0 ends up at the front of the array.

    Examples:

    Input:  [0,1,2,3]
    Output: [0,1,2,3]

    Input:  [1,0,2,3]
    Output: [0,2,3,1]

    Input:  [1,0,2,3,4,5,6]
    Output: [0,2,3,4,5,6,1]

    Input:  [1,8,2,3,4,0,7]
    Output: [0,7,1,8,2,3,4]

    Input:  [1,8,2,3,0,5,6]
    Output: [0,5,6,1,8,2,3]

    Input:  [1,8,2,3,4,5,0]
    Output: [0,1,8,2,3,4,5]
"""


def rotate_left_till_zero_v1(numbers):
    while numbers[0] != 0:
        popped_element = numbers.pop(0)
        numbers.append(popped_element)
    return numbers


from collections import deque


def rotate_left_till_zero_v2(numbers):
    dq = deque(numbers)
    while dq[0] != 0:
        popped_element = dq.popleft()
        dq.append(popped_element)
    return list(dq)


def rotate_left_till_zero_v3(numbers):
    result = []
    offset = 0

    for idx, value in enumerate(numbers):
        if value == 0:
            offset = idx
        result.append(None)

    for idx, value in enumerate(numbers):
        new_pos = (idx - offset + len(numbers)) % len(numbers)
        result[new_pos] = value
    return result


print(rotate_left_till_zero_v3([0, 1, 2, 3]))  # [0, 1, 2, 3]
print(rotate_left_till_zero_v3([1, 0, 2, 3]))  # [0, 2, 3, 1]
print(rotate_left_till_zero_v3([1, 0, 2, 3, 4, 5, 6]))  # [0, 2, 3, 4, 5, 6, 1]
print(rotate_left_till_zero_v3([1, 8, 2, 3, 4, 0, 7]))  # [0, 7, 1, 8, 2, 3, 4]
print(rotate_left_till_zero_v3([1, 8, 2, 3, 0, 5, 6]))  # [0, 5, 6, 1, 8, 2, 3]
print(rotate_left_till_zero_v3([1, 8, 2, 3, 4, 5, 0]))  # [0, 1, 8, 2, 3, 4, 5]
