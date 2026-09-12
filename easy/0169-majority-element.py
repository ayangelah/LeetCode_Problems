class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # keep running count that increments with current majority and decrememts with anything else
        if len(nums) < 3:
            return nums[0]
        majority = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == majority:
                count += 1
            else:
                count -= 1
                if count == -1:
                    majority = nums[i]
                    count = 1
        return majority
