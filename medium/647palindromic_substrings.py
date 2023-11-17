class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        """ecbabcd
        a
        bab
        cbabc
        """
        palindrome_count = 0
        for i in range(len(s)):
            # i is the center
            count = 0
            # odd strings bab 1, 3, 5, 7 ....
            # check if palindrome, going outwards
            while (i-count >= 0 and i+count < len(s) and s[i-count] == s[i+count]):
                palindrome_count += 1
                count += 1
            count = 0
            # even strings baab 2, 4, 6, 8 ....
            while (i-count >= 0 and i+1+count < len(s) and s[i-count] == s[i+1+count]):
                palindrome_count += 1
                count += 1
        return palindrome_count
