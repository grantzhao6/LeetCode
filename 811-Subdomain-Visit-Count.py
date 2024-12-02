class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = {}
        for x in cpdomains:
            s1,s2 = x.split()
            s1 = int(s1)
            sub = s2.split('.')
            for i in range(len(sub)):
                y = '.'.join(sub[i:])
                if y in d:
                    d[y] += s1
                else:
                    d[y] = s1

        result = []

        for k in d:
            result.append(str(d[k]) + " " + k)
        
        return result
