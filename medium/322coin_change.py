class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        dp = [0]
        for i in range(1, amount+1):
            options = []
            for j in range(len(coins)):
                if i-coins[j] >= 0 and dp[i-coins[j]] != -1:
                    options.append(dp[i-coins[j]])
            if options == []:
                dp.append(-1)
            else:
                dp.append(min(options) + 1)
        return dp[amount]
