class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # a[] is array with best solution up till then, holding two-tuples of negative magnitude, and positive magnitude
        a = [(nums[0], nums[0])]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                a.append((max(a[i-1][1] * nums[i], nums[i]),
                         min(a[i-1][0] * nums[i], nums[i])))
            else:
                a.append((max(a[i-1][0] * nums[i], nums[i]),
                         min(a[i-1][1] * nums[i], nums[i])))
            print(a[i])
        maxnum = -10  # guaranteed lowest by constraints
        for j in range(len(a)):
            if a[j][0] > maxnum:
                maxnum = a[j][0]
            if a[j][1] > maxnum:
                maxnum = a[j][1]
        return maxnum
