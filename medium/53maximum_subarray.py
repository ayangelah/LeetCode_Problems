class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # approach: dp in which each index, we choose to continue the old array or start over. we're measuring subarrays starting from 0 (or anything better) and ending at i
        a = [nums[0]]
        for i in range(1, len(nums)):
            a.append(max(a[i-1] + nums[i], nums[i]))
        print(a)
        return max(a)
        # return the max array
