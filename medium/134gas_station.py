from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # try starting at gas station with most gas:
        start = gas.index(max(gas))

        # check if solution exists
        if sum(gas) < sum(cost):
            return -1
        else:
            # re-try solution from the next station after a fail
            i = 0
            possible_start = i
            curr_gas = 0
            while i < len(gas): # iterate through starting points
                curr_gas += gas[i]
                if curr_gas < cost[i]:
                    curr_gas = 0
                    possible_start = i + 1
                else:
                    curr_gas -= cost[i]
                i += 1
            return possible_start