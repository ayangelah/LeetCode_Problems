class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # remove spaces
        a = ""
        for i in range(len(s)):
            if s[i].isalnum():
                a += s[i]
        s = a
        # convert to lower
        s = s.lower()
        print(s)
        for i in range(len(s)):
            if s[i] != s[-i-1]:
                return False
        return True
