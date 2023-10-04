#PROMPT:
#
#Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#
#Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

#11/14/2022
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = False
        if x < 0:
            negative = True
            x = x * -1
        if x >= 2147483648:
            return 0
        while x % 10 == 0:
            x = x/10
            if x == 0:
                return 0
        #reverse
        stringx = str(x)
        stringy = ""
        for i in range(len(stringx)-1, -1, -1):
            stringy += stringx[i]
        y = int(stringy)
        if y >= 2147483648:
            return 0      
        if negative:
            y = y * -1  
        return y