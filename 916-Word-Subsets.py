class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        d = defaultdict(int)
        res = []

        for x in words2:
            c2 = Counter(x)

            for c in c2:
                d[c] = max(d[c],c2[c])
        
        for x in words1:
            c1 = Counter(x)

            for c in d:
                if c1[c] < d[c]:
                    break
            else:
                res.append(x)

        return res

        