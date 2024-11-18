class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        \\\
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        \\\
        d = {}
        e = {}

        for c in ransomNote:
            if c not in d:
                d[c] = 1
            else:
                d[c]+=1

        for c in magazine:
            if c not in e:
                e[c] = 1
            else:
                e[c]+=1    

        for k in d:
            if k not in e:
                return False
            else:
                if d[k] > e[k]:
                    return False


        return True  