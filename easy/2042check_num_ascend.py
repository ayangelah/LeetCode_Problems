class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = []
        curr = ""
        for i in s:
            if i.isdigit():
                print(i)
                curr += i
                continue
            if curr == "":
                continue
            else:
                a.append(int(curr))
                if len(a) > 1 and a[len(a)-1] <= a[len(a)-2]:
                    return False
                curr = ""
        if curr != "":
            a.append(int(curr))
            if len(a) > 1 and a[len(a)-1] <= a[len(a)-2]:
                return False
        return True
