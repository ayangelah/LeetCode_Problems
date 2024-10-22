from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1: # edge case
            return -1
        # bfs solution
        queue = [((0,0), 1)]
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        while queue:
            curr_pos, curr_dist = queue.pop(0)
            if curr_pos == (len(grid)-1, len(grid[0])-1):
                return curr_dist
            for d in directions:
                possible_step = (curr_pos[0] + d[0], curr_pos[1] + d[1])
                if valid_point(possible_step, len(grid), len(grid[0]), grid) and possible_step not in visited:
                    queue.append((possible_step, curr_dist + 1))
                    visited.add(possible_step)

        return -1


def valid_point(coords, n, m, grid): # checks if point is out of bounds or has a 1 in it.
    if coords[0] < 0 or coords[0] >= n:
        return False
    elif coords[1] < 0 or coords[1] >= m:
        return False
    elif grid[coords[0]][coords[1]] == 1:
        return False
    return True