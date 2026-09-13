class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sell at every peak/local majority, buy at every local minority
        bear = prices[0]
        running_total = 0
        for i in range(len(prices)-1):
            if i > 0 and prices[i - 1] > prices[i]: # local min
                bear = prices[i]
            elif i > 0 and prices[i - 1] < prices[i] and prices[i + 1] <= prices[i]: # local max
                # sell
                running_total += prices[i] - bear
                bear = prices[i]
        running_total += max(0, prices[-1] - bear)
        return running_total
