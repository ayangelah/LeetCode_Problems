class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        temp = flowerbed
        maxflowers = 0
        for i, m in enumerate(temp):
            if m == 1:
                continue
            elif temp == [0]:
                maxflowers = 1
                break
            elif i == 0:
                if temp[i+1] == 0:
                    temp[i] = 1
                    maxflowers += 1
                else:
                    continue
            elif i == len(temp) - 1:
                if (temp[i-1] == 0):
                    temp[i] = 1
                    maxflowers += 1
                else:
                    continue
            elif temp[i+1] == 0 and temp[i-1] == 0:
                temp[i] = 1
                maxflowers += 1
        if maxflowers >= n:
            return True
        else:
            return False
