class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        # pick the longest possible GCD
        result = min(str1, str2)
        length = min(len(str1), len(str2))
        decrement = False
        while result != "":
            decrement = False
            for i in range(0, len(str1), len(result)):
                if str1[i:i+len(result)] != result:
                    decrement = True
            for j in range(0, len(str2), len(result)):
                if str2[j:j+len(result)] != result:
                    decrement = True
            if decrement:
                result = result[0:-1]
            else:
                return result
        return result
