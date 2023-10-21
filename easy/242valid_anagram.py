class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = {}
        # fill dictionary with counts
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        # decrement dictionary counts
        for j in t:
            if j in d:
                d[j] -= 1
            else:
                return False

        # check if all letters accounted for
        for k in d.values():
            if k != 0:
                return False
        return True
