class Solution(object):
    def searchMatrix(self, matrix, target):
        \\\
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        \\\
        x = 0
        for i in range(len(matrix)):
            if matrix[i][0] <= target:
                x = i
        
        for j in range(len(matrix[0])):
            if matrix[x][j]==target:
                return True
        
        return False