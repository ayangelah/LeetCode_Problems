from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        # give one candy to each person
        candies = [1]*len(ratings)
        # pass right way to check that those higher than the ones left of them have more candy
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        # pass left way to check that those higher than the ones right of them have more candy
        for j in range(len(ratings) - 2, -1, -1):
            if ratings[j] > ratings[j+1] and candies[j] <= candies[j+1]:
                candies[j] = candies[j+1] + 1
        return sum(candies)