from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # binary search for a peak, move towards greater neighbor
        curr_index = len(nums) // 2
        increment = len(nums) // 4
        while True:
            # left neighbor is greater
            if curr_index > 0 and nums[curr_index - 1] >= nums[curr_index]:
                curr_index -= increment
            # right neighbor is greater
            elif curr_index < len(nums) - 1 and nums[curr_index + 1] >= nums[curr_index]:
                curr_index += increment
            # if found
            else:
                return curr_index
            increment = max(increment // 2, 1)