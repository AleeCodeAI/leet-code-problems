""" 
PROBLEM STATEMENT:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen_numbers = {}
        for idx_1, x in enumerate(numbers):
            complement = target - x
            if complement in seen_numbers:
                idx_2 = seen_numbers[complement]
                return [idx_2, idx_1]
            else:
                seen_numbers[x] = idx_1

"""
WHY DICTIONARY INSTEAD OF NESTED LOOPS:

The dictionary approach achieves O(n) time complexity compared to O(n²) with nested loops.

With nested loops, for each element we'd check all remaining elements to find a match,
resulting in roughly n * n/2 comparisons in the worst case.

Using a dictionary (hash map), we traverse the array only once. For each number, we:
1. Calculate its complement (target - current number)
2. Check if the complement exists in our dictionary - this lookup is O(1)
3. If found, return the indices; if not, store the current number with its index

This trades space (O(n) for the dictionary) for time (O(n) instead of O(n²)), which is
a worthwhile trade-off for better performance, especially with large arrays.
"""
