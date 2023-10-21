class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack)):
            # possible start
            if haystack[i] == needle[0]:
                j = 0
                # check for whole needle
                while i+j < len(haystack) and j < len(needle) and haystack[i+j] == needle[j]:
                    j += 1
                if j == len(needle):
                    return i
        return -1
