class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        islandcount = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":  # checks if an island was discovered
                    # find the entirety of the island through BFS (queue)
                    # turn them all into 0s
                    queue = [(i, j)]  # store coordinates
                    while len(queue) > 0:
                        curr = queue.pop(0)  # takes first element
                        # search in 4 directions:
                        # flipping to 0s keeps track of which coordinates were visited
                        # right
                        if curr[1] + 1 < len(grid[0]) and grid[curr[0]][curr[1]+1] == "1":
                            queue.append((curr[0], curr[1]+1))
                            grid[curr[0]][curr[1]+1] = "0"
                        # left
                        if curr[1] - 1 >= 0 and grid[curr[0]][curr[1]-1] == "1":
                            queue.append((curr[0], curr[1]-1))
                            grid[curr[0]][curr[1]-1] = "0"
                        # down
                        if curr[0] + 1 < len(grid) and grid[curr[0]+1][curr[1]] == "1":
                            queue.append((curr[0]+1, curr[1]))
                            grid[curr[0]+1][curr[1]] = "0"
                        # up
                        if curr[0] - 1 >= 0 and grid[curr[0]-1][curr[1]] == "1":
                            queue.append((curr[0]-1, curr[1]))
                            grid[curr[0]-1][curr[1]] = "0"
                    # increment island count by 1
                    islandcount += 1
        return islandcount
