# my favorite leetcode problem :D
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        result = [1]*length

        right = [1]*length
        left = [1]*length

        # building right sums
        for i in range(length-2, -1, -1):
            # start from length-2 as edges are 1
            right[i] *= right[i+1] * nums[i+1]

        # building left sums
        for i in range(1, length):
            # start from 1 as edges are 1
            left[i] *= left[i-1] * nums[i-1]

        for i in range(0, length):
            result[i] = right[i] * left[i]
        return result
