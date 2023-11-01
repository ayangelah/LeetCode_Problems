class Solution(object):
    def findArray(self, pref):
        """
        :type pref: List[int]
        :rtype: List[int]
        """
        solution = [pref[0]]
        curr = pref[0]
        for i in range(1, len(pref)):
            solution.append(pref[i] ^ curr)
            curr ^= pref[i] ^ curr
        return solution
