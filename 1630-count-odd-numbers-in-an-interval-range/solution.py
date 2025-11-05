class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        numlow=low // 2
        numhigh= (high + 1) // 2 
        return numhigh - numlow
