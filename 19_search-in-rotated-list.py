"""
## Sorted and Rotated List

Given an array with distinct values that is sorted and then rotated,
determine if a target value exists in the array.

A sorted array is rotated by taking an unknown number of values from the
beginning and placing them at the end.

Examples of rotations:
- [3, 4, 5, 1, 2] is rotated left by 2.
- [99, 14, 25, 78, 93] is rotated right by 1.

Parameters:
- arr (List[int]): Input array of distinct integers.
- target (int): The value to search for.

Returns:
- bool: True if the target exists in the array, False otherwise.

Constraints:
- Time Complexity: O(log N)
- Space Complexity: O(1)
"""

"""
Approach:
- Use modified binary search with two pointers: `left` and `right`.
- At every step, compute the middle index `mid`.

Steps:
1. If numbers[mid] equals the target → return True immediately.

2. Decide which half of the list is sorted:
   - If the left half (numbers[left] .. numbers[mid]) is sorted:
     - If the target lies between numbers[left] and numbers[mid] 
       (inclusive of left, exclusive of mid):
       - Move search to the left half → right = mid - 1.
     - Otherwise:
       - Move search to the right half → left = mid + 1.

   - Else the right half (numbers[mid] .. numbers[right]) must be sorted:
     - If the target lies between numbers[mid] and numbers[right] 
       (exclusive of mid, inclusive of right):
       - Move search to the right half → left = mid + 1.
     - Otherwise:
       - Move search to the left half → right = mid - 1.

3. Continue until left passes right. If not found, return False.

Examples:
    search_in_rotated_list([35, 46, 79, 102, 1, 14, 29, 31], 46) True
    search_in_rotated_list([7, 8, 9, 10, 1, 2, 3, 4, 5, 6], 9) True
    search_in_rotated_list([4, 5, 6, 7, 0, 1, 2], 3) False
"""


def search_in_rotated_list(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == target:
            return True

        if numbers[left] <= numbers[mid]:
            if numbers[left] <= target < numbers[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if numbers[mid] < target <= numbers[right]:
                left = mid + 1
            else:
                right = mid - 1

    return False


print(search_in_rotated_list([35, 46, 79, 102, 1, 14, 29, 31], 46) == True)
print(search_in_rotated_list([35, 46, 79, 102, 1, 14, 29, 31], 1) == True)
print(search_in_rotated_list([7, 8, 9, 10, 1, 2, 3, 4, 5, 6], 9) == True)
print(search_in_rotated_list([4, 5, 6, 7, 0, 1, 2], 0) == True)
print(search_in_rotated_list([30, 40, 50, 5, 10, 20], 10) == True)

# Target does not exist
print(search_in_rotated_list([35, 46, 79, 102, 1, 14, 29, 31], 47) == False)
print(search_in_rotated_list([7, 8, 9, 10, 1, 2, 3, 4, 5, 6], 11) == False)
print(search_in_rotated_list([4, 5, 6, 7, 0, 1, 2], 3) == False)

# Edge cases
print(search_in_rotated_list([], 5) == False)  # empty list
print(search_in_rotated_list([1], 1) == True)  # single element, found
print(search_in_rotated_list([1], 2) == False)  # single element, not found
print(search_in_rotated_list([1, 3], 3) == True)  # two elements, rotated
print(search_in_rotated_list([3, 1], 3) == True)  # two elements, rotated differently
print(search_in_rotated_list([3, 1], 2) == False)  # two elements, target absent
