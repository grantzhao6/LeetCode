class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        res = [0]
        for i in range(len(derived)):
            res.append(derived[i]^res[i])
        
        if res[0] == res[-1]:
            return True
        
        res = [1]
        for i in range(len(derived)):
            res.append(derived[i]^res[i])

        if res[0] == res[-1]:
            return True
        
        return False
        