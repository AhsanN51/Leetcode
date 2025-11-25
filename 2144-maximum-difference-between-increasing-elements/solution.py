class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxdif=0
        minnum=nums[0]
        for i in range(1,len(nums)):
            curdef=nums[i]-minnum
            if curdef>maxdif:
                maxdif=curdef
            minnum=min(nums[i],minnum)
        return maxdif if maxdif>0 else -1
