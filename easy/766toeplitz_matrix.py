class Solution(object):
    def isToeplitzMatrix(self, matrix):
        val = None
        for i in range(len(matrix) - 1, 0, -1):
            j = i
            k = 0
            val = matrix[j][k]
            while j < len(matrix) and k < len(matrix[0]):
                if (val != matrix[j][k]):
                    return False
                j += 1
                k += 1
        for a in range(len(matrix[0])):
            b = a
            c = 0
            val = matrix[c][b]
            while b < len(matrix[0]) and c < len(matrix):
                if (val != matrix[c][b]):
                    return False
                b += 1
                c += 1
        return True
