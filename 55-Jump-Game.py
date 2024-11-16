class Solution(object):
    def canJump(self, nums):
        \\\
        :type nums: List[int]
        :rtype: bool
        \\\        
        mjump = nums[0]
        
        for i in range(len(nums)):
            if mjump >= len(nums[i:])-1:
                return True

            if mjump == 0:
                return False
            elif nums[i+1] >= nums[i] and mjump <= nums[i+1]:
                mjump = nums[i+1]
            else:
                mjump -= 1
        
        return False
            
        