class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        offset = None
        for i in range(len(s)):
            if s[i] == goal[0]:
                offset = i
                copy = s[offset:len(s)] + s[0:offset]
                if copy == goal:
                    return True

        return False
