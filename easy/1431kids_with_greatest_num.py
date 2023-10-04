class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maxcandies = max(candies)
        results = [False] * len(candies)
        for i, n in enumerate(candies):
            results[i] = n+extraCandies >= maxcandies
        return results
