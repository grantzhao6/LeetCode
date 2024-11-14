class Solution(object):
    def removeDuplicates(self, nums):
        \\\
        :type nums: List[int]
        :rtype: int
        \\\
        d = {}
        i = 0
        for x in range(len(nums)):
            if nums[x] not in d:
                d[nums[x]] = 1
                nums[i] = nums[x]
                i+=1
            elif d[nums[x]] < 2:
                d[nums[x]] += 1
                nums[i] = nums[x]
                i+=1
        
        return i