class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        currfloor = nums[0]
        second = None
        for i, n in enumerate(nums):
            if n < currfloor:
                currfloor = n
            elif second != None and n > second and n > currfloor:
                return True
            elif n > currfloor:
                second = n
        return False
