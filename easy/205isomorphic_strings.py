class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # dictionary[s] = t
        d = {}
        for i in range(len(s)):
            if s[i] in d and d[s[i]] != t[i]:
                return False
            elif s[i] not in d:
                if t[i] not in d.values():
                    d[s[i]] = t[i]
                else:
                    return False
        return True
