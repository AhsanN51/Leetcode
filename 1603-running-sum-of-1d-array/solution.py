class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        x=0
        a=[]
        for i in nums:
            x+=i
            a.append(x)
        return a
        
