class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 1
        a = [1, 2]
        for i in range(2, n):
            a.append(a[i-1] + a[i-2])
        return a[n - 1]
