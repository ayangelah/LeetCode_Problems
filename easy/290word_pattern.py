class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        d = {}
        s = s.split()
        if (len(pattern) != len(s)):
            return False
        for i in range(len(pattern)):
            if pattern[i] in d and d[pattern[i]] != s[i]:
                print(pattern[i], s[i], d[pattern[i]])
                return False
            elif pattern[i] not in d:
                # bijection check
                if s[i] not in d.values():
                    d[pattern[i]] = s[i]
                else:
                    print(pattern[i])
                    return False
        return True
