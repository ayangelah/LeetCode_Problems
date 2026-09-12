class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # two pointers, where the end of the unique numbers is, and where the duplicate element found is
        if len(nums) < 2:
            return len(nums)
        k = 0
        for i in range(1, len(nums)):
            # if nums[i] = to nums[k], we loop till its is not equal to nums[k], then make nums[k+1] = nums[i]. k advances by 1, and i continues
            if nums[i] != nums[k]:
                nums[k+1] = nums[i]
                k += 1
        return k + 1
