class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        i = 0
        intervals.sort()
        while i < len(intervals)-1:
            if intervals[i][1] >= intervals[i+1][0]:  # overlap!
                intervals[i] = [min(intervals[i][0], intervals[i+1][0]), max(
                    intervals[i][1], intervals[i+1][1])]  # creates the joined interval
                del intervals[i+1]
            else:
                i += 1
        return intervals
