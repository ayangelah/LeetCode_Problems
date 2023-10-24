class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = [0] * (len(cost) + 1)
        for i in range(len(cost), -1, -1):
            if i == len(cost):
                dp[i] = 0
            elif i == len(cost)-1:
                dp[i] = cost[i]
            else:
                # two step
                twostep = cost[i] + dp[i+2]
                # one step
                onestep = cost[i] + dp[i+1]
                dp[i] = min(onestep, twostep)
        return min(dp[0], dp[1])
