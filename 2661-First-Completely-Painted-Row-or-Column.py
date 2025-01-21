class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        d = {}

        row_count = [0]*len(mat)
        col_count = [0]*len(mat[0])

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                d[mat[i][j]] = [i,j]
        
        for k in range(len(arr)):
            num = arr[k]
            x,y = d[num]

            row_count[x] += 1
            col_count[y] += 1

            if row_count[x] == len(mat[0]) or col_count[y] == len(mat):
                return k
        





        