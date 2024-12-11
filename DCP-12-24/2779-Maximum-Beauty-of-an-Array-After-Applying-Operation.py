class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        left = 0
        result = 0
        for i,num in enumerate(nums):
            while left<len(nums) and nums[left]<num-2*k:
                left+=1
            result = max(result,i-left+1)
        return result
        
        