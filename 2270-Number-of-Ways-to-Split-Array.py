class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefixsum = []
        cs = 0
        for x in nums:
            cs += x
            prefixsum.append(cs)
        
        splits = 0
        n = len(nums)
        for i in range(len(nums)-1):
            if prefixsum[i] >= prefixsum[n-1]-prefixsum[i]:
                splits += 1
        
        return splits

        