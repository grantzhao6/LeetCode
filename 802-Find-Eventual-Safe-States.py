class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = [0]*len(graph)
        res = []

        def dfs(i):
            if visited[i] == 1:
                return True
            if visited[i]==-1:
                return False
            visited[i] = 1
            for j in graph[i]:
                if dfs(j):
                    return True
            visited[i] = -1
            return False
        
        for i in range(len(graph)):
            if not dfs(i):
                res.append(i)
        
        return res
        