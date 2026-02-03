"""
PROBLEM STATEMENT:

You are given a 0-indexed array of integers nums of length n, and two positive integers k and dist.

The cost of an array is the value of its first element. For example, the cost of [1,2,3] is 1 while the cost of [3,4,1] is 3.

You need to divide nums into k disjoint contiguous subarrays, such that the difference between the starting index of the second subarray and the starting index of the kth subarray should be less than or equal to dist. In other words, if you divide nums into the subarrays nums[0..(i1 - 1)], nums[i1..(i2 - 1)], ..., nums[ik-1..(n - 1)], then ik-1 - i1 <= dist.

Return the minimum possible sum of the cost of these subarrays.

 

Example 1:

Input: nums = [1,3,2,6,4,2], k = 3, dist = 3
Output: 5
Explanation: The best possible way to divide nums into 3 subarrays is: [1,3], [2,6,4], and [2]. This choice is valid because ik-1 - i1 is 5 - 2 = 3 which is equal to dist. The total cost is nums[0] + nums[2] + nums[5] which is 1 + 2 + 2 = 5.
It can be shown that there is no possible way to divide nums into 3 subarrays at a cost lower than 5.
Example 2:

Input: nums = [10,1,2,2,2,1], k = 4, dist = 3
Output: 15
Explanation: The best possible way to divide nums into 4 subarrays is: [10], [1], [2], and [2,2,1]. This choice is valid because ik-1 - i1 is 3 - 1 = 2 which is less than dist. The total cost is nums[0] + nums[1] + nums[2] + nums[3] which is 10 + 1 + 2 + 2 = 15.
The division [10], [1], [2,2,2], and [1] is not valid, because the difference between ik-1 and i1 is 5 - 1 = 4, which is greater than dist.
It can be shown that there is no possible way to divide nums into 4 subarrays at a cost lower than 15.
Example 3:

Input: nums = [10,8,18,9], k = 3, dist = 1
Output: 36
Explanation: The best possible way to divide nums into 4 subarrays is: [10], [8], and [18,9]. This choice is valid because ik-1 - i1 is 2 - 1 = 1 which is equal to dist.The total cost is nums[0] + nums[1] + nums[2] which is 10 + 8 + 18 = 36.
The division [10], [8,18], and [9] is not valid, because the difference between ik-1 and i1 is 3 - 1 = 2, which is greater than dist.
It can be shown that there is no possible way to divide nums into 3 subarrays at a cost lower than 36.
 

Constraints:

3 <= n <= 105
1 <= nums[i] <= 109
3 <= k <= n
k - 2 <= dist <= n - 2
"""

from typing import List
from sortedcontainers import SortedList

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        # First element is always included
        result = nums[0]
        
        if k == 1:
            return nums[0]
        
        # Use SortedList to maintain k-1 smallest elements in window
        # Split into two parts: selected (k-1 smallest) and candidates (rest)
        selected = SortedList()
        candidates = SortedList()
        selected_sum = 0
        
        # Initialize window [1, dist+1]
        window_size = min(dist + 1, len(nums) - 1)
        
        for i in range(1, window_size + 1):
            selected.add(nums[i])
            selected_sum += nums[i]
        
        # Keep only k-1 elements in selected
        while len(selected) > k - 1:
            val = selected.pop()
            selected_sum -= val
            candidates.add(val)
        
        min_cost = selected_sum
        
        # Slide the window
        for i in range(dist + 2, len(nums)):
            # Add new element
            new_val = nums[i]
            
            if len(selected) < k - 1 or new_val < selected[-1]:
                selected.add(new_val)
                selected_sum += new_val
                
                # Balance: move largest from selected to candidates
                if len(selected) > k - 1:
                    val = selected.pop()
                    selected_sum -= val
                    candidates.add(val)
            else:
                candidates.add(new_val)
            
            # Remove element leaving window
            old_val = nums[i - dist - 1]
            
            if old_val in selected:
                selected.remove(old_val)
                selected_sum -= old_val
                
                # Balance: move smallest from candidates to selected
                if candidates and len(selected) < k - 1:
                    val = candidates.pop(0)
                    selected.add(val)
                    selected_sum += val
            else:
                candidates.remove(old_val)
            
            min_cost = min(min_cost, selected_sum)
        
        return result + min_cost