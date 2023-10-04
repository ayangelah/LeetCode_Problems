# june 27, 2023 solution

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == "":
            return True
        if len(s) > len(t):
            return False
        iterator = 0
        for i in t:
            if iterator >= len(s):
                break
            elif i == s[iterator]:
                iterator += 1
        if iterator == len(s):
            return True
        return False
