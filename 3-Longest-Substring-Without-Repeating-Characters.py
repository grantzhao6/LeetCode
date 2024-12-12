class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = set()
        l = 0
        mcount = 0

        for r in range(len(s)):
            while s[r] in d:
                d.remove(s[l])
                l += 1
            d.add(s[r])
            mcount = max(mcount,r-l+1)

        return mcount


                

