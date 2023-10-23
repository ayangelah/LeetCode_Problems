class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # iterate through array
        i = 0
        count = 0
        while i < len(nums) - count:
            if nums[i] == 0:  # found a zero!
                for j in range(i, len(nums)-1):  # shift
                    nums[j] = nums[j+1]
                nums[len(nums)-1] = 0  # place at end
                count += 1
            else:
                i += 1
        return nums
