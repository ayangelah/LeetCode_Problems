class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        myset = set()
        for x in range(len(nums)):
            dict[x] = 0
        for y in nums:
            myset.add(y)
            if y in dict.keys():
                dict[y] += 1
            else:
                dict[y] = 1
            if dict[y] is 2:
                myset.remove(y)
        for i in myset:
            return i
