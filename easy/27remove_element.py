class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums.sort()
        j = 0
        for i in range(len(nums)):
            # find where the val starts
            if nums[i] == val:
                # count number of items == val
                while i+j < len(nums) and nums[j+i] == val:
                    j += 1
                # shift all of the items:
                for k in range(i, len(nums)-j):
                    nums[k] = nums[k+j]
                    print(k, k+j)
                break

        return len(nums)-j
