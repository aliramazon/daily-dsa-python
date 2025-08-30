"""
Create a function `sort_bit_array` that takes an array containing only bits (0s and 1s)
and sorts it in-place so that all 0s come before all 1s.

The function should run in O(N) time and O(1) extra space.

Examples:

Input:  [0, 1, 0, 1, 1, 0]
Output: [0, 0, 0, 1, 1, 1]

Input:  [1, 1, 1, 0, 0, 0]
Output: [0, 0, 0, 1, 1, 1]

Input:  [0, 0, 0, 0]
Output: [0, 0, 0, 0]        # Already sorted

Input:  [1, 1, 1, 1]
Output: [1, 1, 1, 1]        # Already sorted

Input:  [1, 0, 1, 0, 1]
Output: [0, 0, 1, 1, 1]

Input:  [0, 1]
Output: [0, 1]              # Already sorted
"""


def sort_bit_array_v1(bits):
    zero_count = 0

    for bit in bits:
        if bit == 0:
            zero_count += 1

    i = 0
    while i < zero_count:
        bits[i] = 0
        i += 1

    while i < len(bits):
        bits[i] = 1
        i += 1
    return bits


def sort_bit_array_v2(bits):
    left = 0
    right = len(bits) - 1

    while left < right:
        while left < right and bits[left] == 0:
            left += 1

        while left < right and bits[right] == 1:
            right -= 1

        bits[left], bits[right] = bits[right], bits[left]

    return bits


def sort_bit_array_v3(bits):
    slow = 0

    for idx, value in enumerate(bits):
        if value == 0:
            bits[idx], bits[slow] = bits[slow], bits[idx]
            slow += 1
    return bits


def sort_bit_array_v4(bits):
    insert_pos = 0

    for value in bits:
        if value == 0:
            bits[insert_pos] = 0
            insert_pos += 1

    while insert_pos < len(bits):
        bits[insert_pos] = 1
        insert_pos += 1

    return bits


print(sort_bit_array_v4([0, 1, 0, 1, 1, 0]) == [0, 0, 0, 1, 1, 1])
print(sort_bit_array_v4([1, 1, 1, 0, 0, 0]) == [0, 0, 0, 1, 1, 1])
print(sort_bit_array_v4([0, 0, 0, 0]) == [0, 0, 0, 0])
print(sort_bit_array_v4([1, 1, 1, 1]) == [1, 1, 1, 1])
print(sort_bit_array_v4([1, 0, 1, 0, 1]) == [0, 0, 1, 1, 1])
print(sort_bit_array_v4([0, 1]) == [0, 1])
print(sort_bit_array_v4([]) == [])
print(sort_bit_array_v4([0]) == [0])
print(sort_bit_array_v4([1]) == [1])
