from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:       
        all_players_set = set()
        num_wins_dict = {}
        for i in range(len(matches)):
            all_players_set.add(matches[i][0])
            all_players_set.add(matches[i][1])
            if matches[i][1] not in num_wins_dict:
                num_wins_dict[matches[i][1]] = 1
            else:
                num_wins_dict[matches[i][1]] += 1
        
        one_wins = []
        for item in num_wins_dict.items():
            if item[1] == 1:
                one_wins.append(item[0])
        zero_wins = list(all_players_set - num_wins_dict.keys())
        one_wins.sort()
        zero_wins.sort()
        return [zero_wins, one_wins]