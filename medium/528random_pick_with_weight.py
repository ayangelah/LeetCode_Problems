import random
from typing import List

class Solution:
    def __init__(self, w: List[int]):
        self.total = sum(w)
        self.w = w
        self.running_sums = w.copy()
        for i in range(1, len(self.running_sums)):
            self.running_sums[i] += self.running_sums[i-1]

    def pickIndex(self) -> int:
        weight_index = random.randint(1, self.total)
        curr_index = len(self.running_sums)//2
        increment = len(self.running_sums)//4
        # binary search to find first index
        while True:
            # too small 1 3 6 10 19
            if self.running_sums[curr_index] < weight_index:
                curr_index += increment
            # too large
            elif curr_index > 0 and self.running_sums[curr_index - 1] >= weight_index:
                curr_index -= increment
            else:
                return curr_index
            increment = max(1, increment // 2)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()