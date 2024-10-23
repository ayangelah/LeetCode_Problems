from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # approach: for each pair, grab the earliest start, and the latest end and merge.
        i = 0
        # sort intervals first
        intervals = sorted(intervals, key=lambda x: x[0])
        while i < len(intervals) - 1:
            # overlapping case
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
                intervals.pop(i+1)
            # non-overlapping, so continue
            else:
                i += 1
        return intervals