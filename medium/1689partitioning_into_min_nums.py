class Solution(object):
    def minPartitions(self, n):
        max = 0
        for i in n:
            if int(i) > max:
                max = int(i)
        return max
