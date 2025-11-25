class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=len(nums)
        ans=[]
        ans.append(nums[0])
        for i in range (1,l):
            x= ans[i-1]+nums[i]
            ans.append(x)
        return ans
