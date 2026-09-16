class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        total_prod = prod(nums)
        answer = [total_prod] * len(nums)
        has_zero = False
        if total_prod == 0:
            for i in range(len(nums)):
                if nums[i] == 0 and not has_zero:
                    nums[i] = 1
                    answer[i] = prod(nums)
                    return answer
                elif nums[i] == 0:
                    return answer

        for i in range(len(nums)):
            answer[i] = answer[i] // nums[i]
        return answer
