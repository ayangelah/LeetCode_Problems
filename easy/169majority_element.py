class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr = nums[0]
        count = 1
        for i, n in enumerate(nums):
            if i == 0:
                continue
            if n == curr:
                count += 1
            else:
                if count == 0:
                    curr = n
                else:
                    count -= 1
        return curr
