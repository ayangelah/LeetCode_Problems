class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        # recursive solution, was too slow
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3) """
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        a = [0] * (n+1)
        a[0] = 0
        a[1] = 1
        a[2] = 1
        for i in range(3, n+1):
            a[i] = a[i-1] + a[i-2] + a[i-3]
        return a[n]
