from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = decreasing = True
        for a, b in zip(nums, nums[1:]):
            if a > b:
                increasing = False
            if a < b:
                decreasing = False
        return increasing or decreasing
