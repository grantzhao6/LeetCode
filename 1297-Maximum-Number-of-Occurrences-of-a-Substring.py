class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """
        counter = {}
        l = 0
        result = 0
        for r in range(len(s)+1):
            sub = s[l:r]
            while minSize <= r-l <= maxSize:
                if len(set(sub)) <= maxLetters:
                    counter[sub] = 1 + counter.get(sub, 0)
                    result = max(result, counter[sub])
                l += 1
                sub = s[l:r]
        return result