class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        sum = 0
        for idx, i in enumerate(s):
            if idx+1 >= len(s):
                sum += a[i]
                break
            if a[i] < a[s[idx+1]]:
                sum -= a[i]
            else:
                sum += a[i]
        return sum
