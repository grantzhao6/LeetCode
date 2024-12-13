class Solution:
    def findScore(self, nums: List[int]) -> int:
        score = 0
        s = [(val, i) for i, val in enumerate(nums)]
        heapify(s)
        visited = set()
        while s:
            x,j = heappop(s)

            if j in visited:
                continue

            score += x
            visited.add(j)

            if j - 1 >= 0:
                visited.add(j - 1)
            if j + 1 < len(nums):
                visited.add(j + 1)
        return score


        