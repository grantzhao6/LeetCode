class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        while k > 0:
            cmin = float("inf")
            ci = -1
            for i,x in enumerate(nums):
                if x < cmin:
                    cmin = x
                    ci = i
            nums[ci] = nums[ci] * multiplier
            k-=1

        return nums
                

        