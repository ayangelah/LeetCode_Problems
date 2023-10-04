class Solution(object):
    def findContentChildren(self, g, s):
        count = 0
        g = sorted(g)
        s = sorted(s)
        i = 0
        j = 0
        while i < len(g) and j < len(s):
            if (g[i] <= s[j]):
                count += 1
                i += 1
                j += 1
            else:
                j += 1
        return count
