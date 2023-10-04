class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        iterator = 0
        count = 1
        for i, n in enumerate(chars):
            if i != 0:
                if n != chars[i-1]:
                    chars[iterator] = chars[i-1]
                    iterator += 1
                    if count != 1:
                        for j in str(count):
                            chars[iterator] = j
                            iterator += 1
                    count = 1
                else:
                    count += 1
        chars[iterator] = chars[len(chars)-1]
        iterator += 1
        if count != 1:
            for j in str(count):
                chars[iterator] = j
                iterator += 1
        return iterator
