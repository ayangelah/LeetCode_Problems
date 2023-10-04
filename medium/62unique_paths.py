import math


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        sum = m-1 + n-1
        sol = math.factorial(sum)/(math.factorial(n-1)*math.factorial(m-1))
        return sol
