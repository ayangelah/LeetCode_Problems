class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # approach list in two directions: forward and backwards. forward pointer will remove instances of val and create "holes". backward pointer will note instances that are not val to be placed in holes. forward pointer advances every step. backwards pointer only advances when element at index is equal to val.
        forward = 0
        backward = len(nums) - 1
        while forward < len(nums):
            while backward > 0 and nums[backward] == val:
                backward -= 1
            if nums[forward] == val and forward < backward:
                nums[forward] = nums[backward]
                nums[backward] = val
            if backward <= forward:
                break
            forward += 1
        if not nums:
            return 0
        if nums[forward] != val:
            return forward + 1
        else:
            return forward
