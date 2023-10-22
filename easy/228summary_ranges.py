class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        solution = []
        if nums == []:
            return solution
        temp = str(nums[0])
        arrow = False
        for i in range(1, len(nums)):
            # if don't continue range:
            if nums[i] != nums[i-1] + 1:
                if temp != str(nums[i-1]):
                    temp += str(nums[i-1])
                solution.append(temp)
                arrow = False
                temp = str(nums[i])
            else:
                if not arrow:
                    temp += "->"
                    arrow = True
                if i == len(nums)-1:
                    temp += str(nums[i])
        solution.append(temp)
        return solution
