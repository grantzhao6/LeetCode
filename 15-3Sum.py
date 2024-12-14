class Solution(object):
    def threeSum(self, nums):
        \\\
        :type nums: List[int]
        :rtype: List[List[int]]
        \\\
        nums.sort()
        result = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while l < r:
                s = nums[i]+nums[l]+nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    if [nums[i],nums[l],nums[r]] in result:
                        l += 1
                        r -= 1
                        continue
                    else:
                        result.append([nums[i],nums[l],nums[r]])
                        l += 1
                        r -= 1
        return result

        


        