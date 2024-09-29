from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        i = 0
        offsets = [0] * len(nums)
        while i < len(nums):
            j = 1
            while i+j < len(nums) and nums[i+j] == nums[i]: # absorb duplicates
                offsets[i] += 1
                j += 1
            i += max(1, offsets[i])
        list_shift = 0
        for index, offset in enumerate(offsets):
            if offset != 0:
                del nums[index-list_shift:index+offset-list_shift]
                list_shift += offset
        return len(nums)