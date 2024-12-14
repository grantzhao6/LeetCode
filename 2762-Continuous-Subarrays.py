class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        count = 0
        i = 0
        d = {}
        for j,num in enumerate(nums):
            t = d.copy()
            for k,v in t.items():
                if abs(k-num) > 2:
                    i = max(i,v+1)
                    d.pop(k)
            d[num] = j
            count += j-i+1
        return count
        