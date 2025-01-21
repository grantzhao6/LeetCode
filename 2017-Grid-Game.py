class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        frowsum = sum(grid[0])
        srowsum = 0
        min_sum = float("inf")
        for i in range(len(grid[0])):
            frowsum -= grid[0][i]

            min_sum = min(min_sum,max(frowsum,srowsum))
            srowsum += grid[1][i]
        return min_sum
        