class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while right >= left:
            mid = (left + right)//2  # average spot between with int div
            if right == left:
                return nums[right]
            else:
                if nums[mid] < nums[right]:
                    right = mid
                else:
                    left = mid + 1
