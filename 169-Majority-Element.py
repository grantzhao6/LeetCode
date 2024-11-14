class Solution(object):
    def majorityElement(self, nums):
        \\\
        :type nums: List[int]
        :rtype: int
        \\\
        d = {}
        for x in nums:
            if x not in d:
                d[x] = 1
            else:
                d[x] += 1
        
        for k in d.keys():
            if d[k] > len(nums)/2:
                return k
        