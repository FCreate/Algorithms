#https://leetcode.com/problems/set-matrix-zeroes/
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_rows = set()
        zero_columns = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_columns.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in zero_rows or j in zero_columns:
                    matrix[i][j] = 0
        return matrix
