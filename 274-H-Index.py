class Solution(object):
    def hIndex(self, citations):
        \\\
        :type citations: List[int]
        :rtype: int
        \\\
        citations.sort()
        for i,citation in enumerate(citations):
            if citation >= len(citations) - i:
                return len(citations)-i
        return 0
            
            

            
        