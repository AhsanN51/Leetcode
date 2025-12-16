class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        so=sorted(nums)
        s=[]
        st=0
        ed=len(nums)-1
        for i in range(len(nums)):
            s=nums[i:ed+1]+nums[st:i]
            print(s)
            if s==so:
                return True
        return False
