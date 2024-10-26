from cmath import sqrt
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # dict holding key: distance, value: list of indexes of point
        # list of sorted distances
        distance_dict = {}
        distance_list = []
        for i in range(len(points)):
            distance = sqrt(points[i][0]**2 + points[i][1]**2)
            if distance not in distance_dict:
                distance_dict[distance] = [i]
            else:
                distance_dict[distance].append(i)
            distance_list.append(distance)
        
        result = []
        distance_list.sort()
        curr_k = k
        for d in distance_list:
            j = 0
            while curr_k > 0 and j < len(distance_dict[d]):
                result.append(points[distance_dict[d][j]])
                j += 1
                curr_k -= 1
        return result