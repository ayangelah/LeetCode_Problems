class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowelset = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        vowel = ""
        indices = []
        copy = s
        for i, n in enumerate(s):
            if n in vowelset:
                vowel += n
                indices.append(i)
        for j, m in enumerate(indices):
            newvowel = vowel[len(vowel)-j-1]
            copy = copy[:m] + newvowel + copy[m+1:]
        return copy
