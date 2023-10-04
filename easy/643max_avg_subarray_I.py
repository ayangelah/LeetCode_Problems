class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        if (len(nums) == 1):
            return float(nums[0])
        curr = 0.0
        for j in range(k):
            curr += nums[j]
        max = curr
        for i, n in enumerate(nums):
            if (i > len(nums)-k):
                break
            elif (i == 0):
                continue
            else:
                curr -= nums[i-1]
                curr += nums[i+k-1]
                if curr > max:
                    max = curr

        return max/k
