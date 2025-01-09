class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for x in words:
            if pref in x and x.find(pref)==0:
                count+=1
        return count
                        