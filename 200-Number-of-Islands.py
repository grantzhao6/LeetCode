class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0
        rows = len(grid)
        cols = len(grid[0])
        def bfs(x, y):
            que = deque()
            que.append((x,y))
            visited.add((x,y))
            while que:
                a,b = que.popleft()
                for (dx,dy) in [(0,1),(1,0),(0,-1),(-1,0)]:
                    x,y = a + dx, b + dy
                    if 0 <= x < rows and 0 <= y < cols and grid[x][y] == \1\ and (x, y) not in visited:
                        que.append((x,y))
                        visited.add((x,y))
        
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == \1\ and (x,y) not in visited:
                    islands +=1
                    bfs(x,y)
        
        return islands


                
        