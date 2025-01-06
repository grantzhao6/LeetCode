class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n  = len(s)
        dp = [0]*(n+1)
        for shift in shifts:
            st,e,d = shift
            if d == 1:
                dp[st] +=1
                dp[e+1] -= 1
            else:
                dp[st] -= 1
                dp[e+1] += 1
        psum = 0
        s = list(s)
        for i in range(n):
            psum += dp[i]
            cpos = ord(s[i])-ord('a')
            npos = (cpos + psum%26+26)%26
            s[i] = chr(ord('a')+npos)
        
        return "".join(s)

        # s = list(s)
        # for x in shifts:
        #     i = x[0]
        #     j = x[1]
        #     d = x[2]
        #     for y in range(i,j+1):
        #         c = s[y]

        #         cpos = ord(c)-ord('a')

        #         if d == 1:
        #             npos = (cpos+1)%26
        #         else:
        #             npos = (cpos-1+26)%26

        #         s[y] = chr(ord('a')+npos)
        # return "".join(s)
                

        