class Solution(object):
    def rotate(self, nums, k):
        \\\
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        \\\
        def helper(nums,i,j):
            while (i<j):
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
                j-=1
            return nums
        
        if k > len(nums):
            k%= len(nums)
        
        if (k>0):
            helper(nums,0,len(nums)-1)
            helper(nums,0,k-1)
            helper(nums,k,len(nums)-1)

