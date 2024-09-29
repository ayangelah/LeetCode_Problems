from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # sort
        citations.sort()
        h = len(citations)
        for i in range(len(citations)):
            if citations[i] >= h and len(citations) - i + 1 >= h:
                return h
            else:
                h -= 1
        return 0
