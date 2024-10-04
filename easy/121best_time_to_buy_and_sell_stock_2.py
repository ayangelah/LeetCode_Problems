
from typing import List

# redo of a problem I already did. 10/3/2024.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        s = 1
        b = 0
        while s < len(prices):
            if prices[s] - prices[b] > max_profit:
                max_profit = prices[s] - prices[b]
            # move b if a new low is found
            if prices[s] < prices[b]:
                b = s
            # move s
            s += 1
        return max_profit