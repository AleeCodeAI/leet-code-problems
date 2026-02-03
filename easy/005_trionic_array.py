"""
You are given an integer array nums of length n.

An array is trionic if there exist indices 0 < p < q < n − 1 such that:

nums[0...p] is strictly increasing,
nums[p...q] is strictly decreasing,
nums[q...n − 1] is strictly increasing.
Return true if nums is trionic, otherwise return false.

 

Example 1:

Input: nums = [1,3,5,4,2,6]

Output: true

Explanation:

Pick p = 2, q = 4:

nums[0...2] = [1, 3, 5] is strictly increasing (1 < 3 < 5).
nums[2...4] = [5, 4, 2] is strictly decreasing (5 > 4 > 2).
nums[4...5] = [2, 6] is strictly increasing (2 < 6).
Example 2:

Input: nums = [2,1,3]

Output: false

Explanation:

There is no way to pick p and q to form the required three segments.

 

Constraints:

3 <= n <= 100
-1000 <= nums[i] <= 1000
"""


from typing import List

class Solution: 
    def __init__(self):
        self.phase = 1
    def isTrionic(self, nums: List[int]) -> bool:
        for iteration in range(len(nums)):
            num1 = nums[iteration]
            if iteration == len(nums)-1:
                break
            num2 = nums[iteration+1]
            if self.phase == 1 and iteration == 0 and num1 > num2:
                return False
            if num1 == num2:
                return False
            elif self.phase == 1 and num1 < num2:
                pass
            elif self.phase == 1 and num1 > num2:
                self.phase = 2
            elif self.phase == 2 and num1 > num2:
                pass 
            elif self.phase == 2 and num1 < num2:
                self.phase = 3
            elif self.phase == 3 and num1 < num2:
                pass
            elif self.phase == 3 and num1 > num2:
                return False
        if self.phase == 3:
            return True
        return False
