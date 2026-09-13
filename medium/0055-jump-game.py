class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = nums[0]
        if max_jump == 0 and len(nums) > 1:
            return False
        for i in range(1, len(nums)):
            max_jump -= 1
            if nums[i] > max_jump:
                max_jump = nums[i]
            if max_jump == 0 and i < len(nums) - 1:
                return False
        return True
            
            
