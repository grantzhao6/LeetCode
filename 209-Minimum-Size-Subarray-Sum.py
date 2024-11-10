class Solution(object):
    def minSubArrayLen(self, target, nums):
        \\\
        :type target: int
        :type nums: List[int]
        :rtype: int
        \\\
        min_len = float(\inf\)
        i = 0
        total = 0

        for j in range(len(nums)):
            total += nums[j]
            while total >= target:
                if j-i+1<min_len:
                    min_len = j-i+1
                total -= nums[i]
                i+=1
                
        return min_len if min_len != float(\inf\) else 0
            
        