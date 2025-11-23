class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # Base case
        if n == 0:
            return 1.0
        
        # Handle negative exponent
        if n < 0:
            return 1 / self.myPow(x, -n)
        
        # Recursive call for half power
        half = self.myPow(x, n // 2)
        
        # If n is even
        if n % 2 == 0:
            return half * half
        else:
            # If n is odd
            return half * half * x

