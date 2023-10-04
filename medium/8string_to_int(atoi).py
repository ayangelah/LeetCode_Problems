class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        negative = False
        number = ""
        j = 0
        while j < len(s):
            if s[j] == '-':
                negative = True
                j += 1
                break
            elif s[j] == '+':
                negative = False
                j += 1
                break
            elif s[j] == ' ':
                j += 1
                continue
            else:
                break
            j += 1
        i = j
        while i < len(s):
            if s[i].isdigit():
                number += s[i]
            else:
                break
            i += 1
        if number == "":
            return 0
        sol = int(number)
        if negative:
            sol *= -1
        if sol > 2147483647:
            sol = 2147483647
        if sol < -2147483648:
            sol = -2147483648
        return sol
