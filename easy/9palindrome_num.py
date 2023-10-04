class Solution:
    def isPalindrome(self, x: int) -> bool:
        "go from both ends"
        "head equal tail till meet in the middle"
        digit = 0
        string = str(x)
        while (len(string) - digit - 1) - digit > 0:
            if string[digit] != string[len(string) - digit - 1]:
                return False
            digit = digit + 1
        return True
