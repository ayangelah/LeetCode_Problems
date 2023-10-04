class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1:
                    perimeter += 4
                    if j > 0:
                        if grid[i][j - 1] == 1:
                            perimeter -= 1
                    if i > 0:
                        if grid[i - 1][j] == 1:
                            perimeter -= 1
                    if j < len(grid[0]) - 1:
                        if grid[i][j + 1] == 1:
                            perimeter -= 1
                    if i < len(grid) - 1:
                        if grid[i + 1][j] == 1:
                            perimeter -= 1
        return perimeter
