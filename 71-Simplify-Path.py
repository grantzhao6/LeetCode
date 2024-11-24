class Solution(object):
    def simplifyPath(self, path):
        \\\
        :type path: str
        :rtype: str
        \\\
        stack = []
        l = path.split(\/\)
        for x in l:
            if x  == \.\ or not x:
                continue

            if x == \..\:
                if stack:
                    stack.pop()
            else:
                stack.append(x)
        
        return \/\+\/\.join(stack)
        