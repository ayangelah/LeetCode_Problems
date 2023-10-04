class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}

        currcount = 0
        for j in range(k):
            if s[j] in vowels:
                currcount += 1
        max = currcount
        for i, n in enumerate(s):
            if i == 0:
                continue
            elif i > len(s)-k:
                break
            else:
                if s[i-1] in vowels:
                    currcount -= 1
                if s[i+k-1] in vowels:
                    currcount += 1
                if currcount > max:
                    max = currcount
        if max >= k:
            return k
        else:
            return max
