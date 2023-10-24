class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        d = {}
        for row in grid:
            if str(row) in d:  # change to string because list is mutable
                d[str(row)][0] += 1
            else:
                d[str(row)] = [1, 0]
        # iterating through each column
        for i in range(len(grid)):
            col = []
            # iterating through each index in column
            for j in range(len(grid)):
                col.append(grid[j][i])
            if str(col) in d:
                d[str(col)][1] += 1
            else:
                d[str(col)] = [0, 1]

        # iterate through dictionary
        totalpairs = 0
        for val in d.values():
            totalpairs += val[0]*val[1]
        return totalpairs
