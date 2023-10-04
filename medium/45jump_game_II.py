class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = len(nums) - 1
        cursor = i
        jumpcount = 0
        while cursor > 0:
            j = 0
            while j < cursor:
                if (nums[j] >= cursor - j):
                    cursor = j
                    jumpcount += 1
                j += 1
        return jumpcount
