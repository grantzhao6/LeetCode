class Solution(object):
    def jump(self, nums):
        \\\
        :type nums: List[int]
        :rtype: int
        \\\
        njump = 0
        fjump = 0
        d = len(nums)-1
        counter = 0
        
        while fjump < d:
            farthest = 0
            for i in range(njump,fjump+1):
                farthest = max(farthest,i + nums[i])
            njump = fjump+1
            fjump = farthest
            counter+=1

        return counter
            

        