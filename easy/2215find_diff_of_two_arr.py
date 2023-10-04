class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        set1 = set()
        set2 = set()
        answer = [[], []]
        for i in nums1:
            set1.add(i)
        for j in nums2:
            set2.add(j)
        for k in nums1:
            if k not in set2 and k not in answer[0]:
                answer[0].append(k)
        for l in nums2:
            if l not in set1 and l not in answer[1]:
                answer[1].append(l)
        return answer
