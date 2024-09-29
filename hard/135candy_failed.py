from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        # give one candy to each person
        candies = [1]*len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i]<ratings[i-1]: # if an even lower low is found
                j = i
                while j > 0 and ratings[j]<ratings[j-1] and candies[j]>=candies[j-1]: # then propagate the change backwards
                    candies[j-1] += 1
                    j -= 1
            elif ratings[i]>ratings[i-1]:
                candies[i] = candies[i-1] + 1
        return sum(candies)