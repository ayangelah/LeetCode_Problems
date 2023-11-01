class Solution(object):
    def minimumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        output = -1  # 3*50

        for i in range(len(nums)-2):
            for j in range(i, len(nums)-1):
                if j == i:
                    continue
                if nums[j] <= nums[i]:
                    break
                for k in range(j, len(nums)):
                    if k == j:
                        continue
                    if nums[k] < nums[j]:
                        if output == -1 or nums[i] + nums[j] + nums[k] < output:
                            output = nums[i] + nums[j] + nums[k]
                            print(output)
        return output
