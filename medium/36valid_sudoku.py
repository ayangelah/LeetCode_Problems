class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        temp1 = set()
        temp2 = set()
        temp3 = set()
        for i in range(0, 9):
            temp1.clear()
            temp2.clear()
            for j in range(0, 9):
                if board[i][j] in temp1 and board[i][j] != ".":
                    return False
                else:
                    temp1.add(board[i][j])
                if board[j][i] in temp2 and board[j][i] != ".":
                    return False
                else:
                    temp2.add(board[j][i])
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                temp3.clear()
                for k in range(0, 3):
                    for l in range(0, 3):
                        if board[i+k][j+l] in temp3 and board[i+k][j+l] != ".":
                            return False
                        else:
                            temp3.add(board[i+k][j+l])
        return True
