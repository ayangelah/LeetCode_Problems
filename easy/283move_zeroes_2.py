from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # move all zeros to end preserve order, in place
        # approach: go from the end, and move zeros to the end 
        search = 0
        insertion = -1
        while search < len(nums):
            # if we find a zero, and zero_index is None, zero_index = i
            if nums[search] == 0 and insertion == -1:
                insertion = search
            # if we find a non-zero number and zero_index is not None, then swap the two indices, set zero_index to None
            elif nums[search] != 0 and insertion != -1:
                temp = nums[search]
                nums[search] = nums[insertion]
                nums[insertion] = temp
                insertion += 1
            search += 1
            