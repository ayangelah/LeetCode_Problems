from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        conversion_dict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        # iterate through the list and for each added character, multiply the amount of current entries in the set by the number of possibilities and replace set
        curr_set = []
        next_set = []
        for d in digits:
            for j in conversion_dict[d]:
                if len(curr_set) == 0:
                    next_set.append(j)
                else:
                    for k in range(len(curr_set)):
                        next_set.append(curr_set[k] + j)
            curr_set = next_set
            next_set = []
        return curr_set
