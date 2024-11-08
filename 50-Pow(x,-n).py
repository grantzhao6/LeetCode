class Solution(object):
    def myPow(self, x, n):
        \\\
        :type x: float
        :type n: int
        :rtype: float
        \\\
        def helper(x,n):
            if n == 0:
                return 1
            elif n%2 == 0:
                return helper(x*x,n//2)
            else:
                return x*helper(x*x,(n-1)//2)

        result = helper(x,abs(n))
        
        return result if n >=0 else 1/result