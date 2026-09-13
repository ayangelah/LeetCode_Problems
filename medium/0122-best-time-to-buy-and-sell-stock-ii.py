class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sell at every peak/local majority, buy at every local minority
        profits = [0] * len(prices)
        bear = prices[0]
        bull = prices[0]
        running_total = 0
        for i in range(len(prices)-1):
            if i > 0 and prices[i - 1] > prices[i]: # local min
                bear = prices[i]
            elif i > 0 and prices[i - 1] < prices[i] and prices[i + 1] <= prices[i]: # local max
                # sell
                bull = prices[i]
                running_total += bull - bear
                bear = prices[i]
        running_total += max(0, prices[-1] - bear)
        return running_total
