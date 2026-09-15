class Solution:
    def jump(self, nums: List[int]) -> int:
        # greedy solution, because the dp would be O(N^2)
        i = 0
        min_jumps = 0
        while i < len(nums) - 1:
            lookahead = min(len(nums), i + nums[i] + 1)
            if lookahead == len(nums):
                return min_jumps + 1
            max_jump = 0
            max_i = i
            for j in range(i+1, lookahead):
                if nums[j] + j >= max_jump:
                    max_jump = nums[j] + j
                    max_i = j
            i = max_i
            min_jumps += 1
        return min_jumps
            
