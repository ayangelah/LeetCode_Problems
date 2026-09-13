class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k == 0:
            return
        end = len(nums) - 1
        start = 0
        # flip list once
        self.flip(nums, start, end)
        # flip list again within k
        end = k - 1
        start = 0
        self.flip(nums, start, end)
        # flip list again after k
        end = len(nums) - 1
        start = k
        self.flip(nums, start, end)
    
    def flip(self, nums: list[int], start: int, end: int):
        while end - start > 0:
            temp = nums[end]
            nums[end] = nums[start]
            nums[start] = temp
            end -= 1
            start += 1
