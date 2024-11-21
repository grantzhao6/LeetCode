class Solution(object):
    def groupAnagrams(self, strs):
        \\\
        :type strs: List[str]
        :rtype: List[List[str]]
        \\\
        d = defaultdict(list)

        for x in strs:
            k = \\.join(sorted(x))
            d[k].append(x)
        
        return list(d.values())
        
        
