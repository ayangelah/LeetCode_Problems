class Solution(object):
    def groupAnagrams(self, strs):
        solution = []
        dictionaryset = []
        anagramset = []
        curr = {}
        for i in range(len(strs)):
            curr.clear()
            for j in strs[i]:
                if j in curr:
                    curr[j] += 1
                else:
                    curr[j] = 1
            a = False
            for k in range(len(dictionaryset)):
                if dictionaryset[k] == curr:
                    anagramset[k].append(strs[i])
                    a = True
                    break
            if not a:
                dictionaryset.append(curr.copy())
                anagramset.append([strs[i]])
        for l in range(len(anagramset)):
            solution.append(anagramset[l])
        return solution
