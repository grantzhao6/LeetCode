class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []
        for x in intervals:
            if len(result) == 0:
                result.append(x)
            else:
                cinterval = result[-1]
                if x[0] >= cinterval[0] and x[0]<=cinterval[1]:
                    nmax = max(cinterval[1],x[1])
                    cinterval[1] = nmax
                    result[-1] = cinterval
                else:
                    result.append(x)
        return result
                
        