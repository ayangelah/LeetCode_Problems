from typing import List

# redo of a problem I already did. 10/3/2024.
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        l = 0
        r = len(height) - 1
        while l < r:
            curr_vol = min(height[r], height[l]) * (r-l)
            if curr_vol > max_water:
                max_water = curr_vol
            # move l if a r is higher
            if height[l] < height[r]:
                l += 1
            # otherwise, move r
            else:
                r -= 1
        return max_water