class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s1 = set()
        s2 = set()
        dup = [0]
        missing = [0]
        for i in range(len(nums)):
            if nums[i] in s2:
                dup = [nums[i]]
            else:
                s2.add(nums[i])
            s1.add(i+1)
        missing = [(s1 - s2).pop()]
        return dup + missing
