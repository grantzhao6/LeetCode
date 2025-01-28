class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def bfs(i,j,grid):
            q = [(i,j)]
            fish = grid[i][j]
            grid[i][j] = 0

            while q:
                x,y = q.pop(0)
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nx,ny = x+dx,y+dy
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] > 0:
                        q.append((nx,ny))
                        fish += grid[nx][ny]
                        grid[nx][ny] = 0
            return fish

        maxfish = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]>0:
                    maxfish = max(maxfish,bfs(i,j,grid))
        
        return maxfish


        