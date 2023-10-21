class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazinedict = {}

        # build hashmap
        for i in magazine:
            if i in magazinedict:
                magazinedict[i] += 1
            else:
                magazinedict[i] = 1

        # check ransomnote by decrementing
        for j in ransomNote:
            if j in magazinedict:
                if magazinedict[j] > 0:
                    magazinedict[j] -= 1
                else:
                    return False
            else:
                return False
        return True
