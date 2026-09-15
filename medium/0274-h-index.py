class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # two axes, and finding the greatest "square" formed by their plotting
        # sort the list, then find the greatest index at which len(citation) - index is greater than or equal to the index's value
        citations.sort()
        h_index = 0
        for i in range(len(citations)):
            if citations[i] >= (len(citations) - i) and citations[i] > h_index:
                h_index += 1
        return h_index
