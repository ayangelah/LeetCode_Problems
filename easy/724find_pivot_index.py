class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # finding sum
        numsum = sum(nums)
        # check for pivot
        left = 0
        right = numsum
        for j, n in enumerate(nums):
            if j != 0:
                left += nums[j-1]
            right -= n
            if left == right:
                return j
        return -1
