from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(1, len(words)):
            for j in range(min(len(words[i]), len(words[i-1]))):
                in_order = False
                if ordering(words[i-1][j], words[i][j], order) == 0:
                    continue
                elif ordering(words[i-1][j], words[i][j], order) == -1:
                    return False
                else:
                    in_order = True
                    break
            if not in_order and j == min(len(words[i]), len(words[i-1])) - 1 and len(words[i-1]) > len(words[i]):
                return False
        return True

def ordering(char1, char2, order):
    if char1 == char2:
        return 0
    for i in order:
        if char1 == i:
            return 1
        elif char2 == i:
            return -1