class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        d = {}
        mval = 0
        for x in nums:
            i = d.get(x-1,0)
            j = d.get(x+1,0)
            val = i+j+1
            d[x-i] = val
            d[x+j] = val
            mval = max(mval,val)
        return mval
        