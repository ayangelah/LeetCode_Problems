from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited_set = set()
        max_island_size = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (i, j) not in visited_set:
                    island_area, new_visited_set = bfs_island(grid, (i, j), visited_set, n, m)
                    visited_set = new_visited_set
                    if island_area > max_island_size:
                        max_island_size = island_area
        return max_island_size
        
def bfs_island(grid, start, visited_set, n, m): # start is guaranteed to be on land
    '''returns: area, visited_set'''
    queue = [start]
    visited_on_this_island = set([start])
    while queue:
        curr = queue.pop(0)
        # if not out of bounds, and has 1 and is not visited yet, put in queue
        # left
        if curr[1] - 1 >= 0 and grid[curr[0]][curr[1] - 1] == 1 and (curr[0], curr[1] - 1) not in visited_on_this_island:
            queue.append((curr[0], curr[1] - 1))
            visited_on_this_island.add((curr[0], curr[1] - 1))
        # right
        if curr[1] + 1 < m and grid[curr[0]][curr[1] + 1] == 1 and (curr[0], curr[1] + 1) not in visited_on_this_island:
            queue.append((curr[0], curr[1] + 1))
            visited_on_this_island.add((curr[0], curr[1] + 1))
        # up
        if curr[0] - 1 >= 0 and grid[curr[0] - 1][curr[1]] == 1 and (curr[0] - 1, curr[1]) not in visited_on_this_island:
            queue.append((curr[0] - 1, curr[1]))
            visited_on_this_island.add((curr[0] - 1, curr[1]))
        # down
        if curr[0] + 1 < n and grid[curr[0] + 1][curr[1]] == 1 and (curr[0] + 1, curr[1]) not in visited_on_this_island:
            queue.append((curr[0] + 1, curr[1]))
            visited_on_this_island.add((curr[0] + 1, curr[1]))
    return (len(visited_on_this_island), visited_on_this_island.union(visited_set))