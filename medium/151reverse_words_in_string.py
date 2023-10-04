class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        wordlist = []
        curr = ""
        for j, i in enumerate(s):
            if i != " ":
                curr += i
                if j == len(s)-1 and curr != "":
                    wordlist.append(curr)
                    curr = ""
            elif curr != "":
                wordlist.append(curr)
                curr = ""

        output = ""
        for k in range(len(wordlist)-1, -1, -1):
            output += wordlist[k]
            if k > 0:
                output += " "
        return output
