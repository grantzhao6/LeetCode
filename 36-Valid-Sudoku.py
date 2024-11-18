class Solution(object):
    def isValidSudoku(self, board):
        \\\
        :type board: List[List[str]]
        :rtype: bool
        \\\
        # visited = set()

        # #check each col
        # for i in range(9):
        #     for j in range(9):
        #         if board[i][j]!= \.\:
        #             if board[i][j] not in visited:
        #                 visited.add(board[i][j])
        #             else:
        #                 return False
        #     visited.clear()
        
        # visited.clear()

        # #check each row
        # for i in range(9):
        #     for j in range(9):
        #         if board[j][i]!= \.\:
        #             if board[j][i] not in visited:
        #                 visited.add(board[j][i])
        #             else:
        #                 return False
        #     visited.clear()
        
        # visited.clear()

        # #check each 3x3
        # i = 0
        # j = 0
        # while i < 9:
        #     while j < 9:
        #         for x in range(i,i+3):
        #             for y in range(j,j+3):
        #                 if board[x][y]!= \.\:
        #                     if board[x][y] not in visited:
        #                         visited.add(board[x][y])
        #                     else:
        #                         return False
        #         visited.clear()
        #         j+=3       
        #     j=0    
        #     i+=3
        
        # return True

        #faster solution
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == \.\:
                    continue
                
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in boxes[(r // 3, c // 3)]:
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[(r // 3, c // 3)].add(board[r][c])
        
        return True




        


        