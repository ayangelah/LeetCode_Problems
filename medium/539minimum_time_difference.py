from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        min_time_difference = time_difference(timePoints[0], timePoints[-1])
        for i in range(1, len(timePoints)):
            curr = time_difference(timePoints[i], timePoints[i-1])
            min_time_difference = min(curr, min_time_difference)
        return min_time_difference

    
def time_difference(time_1, time_2):
    t1 = (int(time_1[:2]), int(time_1[3:]))
    t2 = (int(time_2[:2]), int(time_2[3:]))
    
    bigger = t2
    smaller = t1
    if t1[0] > t2[0]:
        bigger = t1
        smaller = t2
    
    result_hour = bigger[0] - smaller[0]
    if bigger[1] < smaller[1]:
        result_min = bigger[1] + 60 - smaller[1]
        result_hour -= 1
    else:
        result_min = bigger[1] - smaller[1]
    
    return abs(min(result_hour*60 + result_min, 1440-(result_hour*60 + result_min)))