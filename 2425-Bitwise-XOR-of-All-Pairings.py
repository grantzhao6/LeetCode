class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        len1 = len(nums1)
        len2 = len(nums2)

        d = {}

        for x in nums1:
            d[x] = d.get(x,0) + len2
        
        for y in nums2:
            d[y] = d.get(y,0) + len1

        ans = 0
        for x in d:
            if d[x] % 2:
                ans ^= x 
        return ans       