class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # for each index write the max sell you can get that day, find the max between the two
        profits = [0] * len(prices)
        min = prices[0]
        for i in range(len(prices)):
            if prices[i] < min:
                min = prices[i]
            if i == 0:
                profits[i] == 0
            else:
                profits[i] = max(prices[i] - min, profits[i-1])
        return profits[-1]
