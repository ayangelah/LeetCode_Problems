class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        occ = {}
        for i in arr:
            if i in occ:
                occ[i] += 1
            else:
                occ[i] = 1
        occset = set()
        for j in occ:
            if occ[j] in occset:
                return False
            else:
                occset.add(occ[j])
        return True
