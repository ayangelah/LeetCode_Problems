from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # check if there's an increase in price, if so, hold.
        bought = False
        profits = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                bought = True
                profits += prices[i] - prices[i-1]
            else:
                bought = False
        return profits