class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        idx = 0
        while idx < len(s):
            bubble = False
            if idx < len(s) - 1:
                if (s[idx].islower() and s[idx + 1].isupper()) and (s[idx].lower() == s[idx + 1].lower()):
                    if idx + 2 > len(s):
                        print("got here 1")
                        s = s[0:idx]
                    else:
                        print("got here 2")
                        s = s[0:idx] + s[idx + 2:]
                    idx = 0
                    continue
            if idx >= 1:
                if (s[idx].islower() and s[idx - 1].isupper()) and (s[idx].lower() == s[idx - 1].lower()):
                    if idx + 1 > len(s):
                        print("got here 3")
                        s = s[0:idx - 1]
                    else:
                        print("got here 4")
                        s = s[0:idx - 1] + s[idx + 1:]
                    idx = 0
                    continue
            idx += 1
        return s
