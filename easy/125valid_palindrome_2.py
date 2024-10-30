class Solution:
    def isPalindrome(self, s: str) -> bool:
        # process string O(N)
        clean_str = ""
        for i in range(len(s)):
            if not s[i].isalpha():
                continue
            clean_str += s[i].lower()
        print(clean_str)
        
        # r and l pointer, going inwards, so long as r-l is greater than 0 (need to check the innermost 2 for an even palindrome)
        r = len(clean_str) - 1
        l = 0
        while r - l > 0:
            if clean_str[r] != clean_str[l]:
                return False
            r -= 1
            l += 1
        return True