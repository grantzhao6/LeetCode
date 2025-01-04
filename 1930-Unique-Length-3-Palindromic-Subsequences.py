class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        d = set(s)
        sub = 0

        for x in d:
            i = s.index(x)
            j = s.rindex(x)
            b = set()

            for y in range(i+1,j):
                b.add(s[y])

            sub += len(b)

        return sub


        

        