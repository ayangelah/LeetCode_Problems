class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        maxalt = 0
        curralt = 0
        for i in gain:
            curralt += i
            if curralt > maxalt:
                maxalt = curralt
        return maxalt
