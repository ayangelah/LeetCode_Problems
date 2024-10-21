class Solution:
    def validPalindrome(self, s: str) -> bool:
        # approach: helper function that returns if its a valid bool, if a mismatch is found, return the or of the resulting two possible changes.
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return palindrome_checker(s[l+1:r+1]) or palindrome_checker(s[l:r])
            l += 1
            r -= 1
        return True

def palindrome_checker(s):
    l = 0
    r = len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True