class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        a = set()
        num = n
        while num != 1:
            numsum = 0
            for i in range(len(str(num))):
                numsum += (int(str(num)[i-1])) ** 2
            num = numsum
            if (num in a):
                return False
            a.add(num)
        return True
