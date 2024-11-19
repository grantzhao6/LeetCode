class Solution(object):
    def spiralOrder(self, matrix):
        \\\
        :type matrix: List[List[int]]
        :rtype: List[int]
        \\\
        rows = len(matrix)
        cols = len(matrix[0])

        ri=0
        ci=-1

        direction = 1
    
        result = []

        while rows>0 and cols>0:
            for _ in range(cols):
                ci += direction
                result.append(matrix[ri][ci])
                
            rows-=1
            for _ in range(rows):
                ri+=direction
                result.append(matrix[ri][ci])
                
            cols-=1

            direction *=-1
        
        return result
        



        
        