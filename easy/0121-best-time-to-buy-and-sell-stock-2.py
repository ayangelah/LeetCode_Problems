class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # for each index write the max sell you can get that day, find the max between the two
        min = prices[0]
        for i in range(len(prices)):
            if prices[i] < min:
                min = prices[i]
            if i == 0:
                prices[i] = 0
            else:
                prices[i] = max(prices[i] - min, prices[i-1])
        return prices[-1]
