class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
            
        m = [[] for _ in range(numRows)]

        i = 0
        d = 1
        result = \\

        for c in s:
            m[i].append(c)
            if i == 0:
                d = 1
            elif i == numRows-1:
                d = -1
            i += d
        
        for i in range(numRows):
            result += \\.join(m[i])
        
        return result

        