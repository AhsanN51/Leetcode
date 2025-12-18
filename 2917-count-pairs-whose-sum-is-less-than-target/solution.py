class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        i=0
        j=len(nums)-1
        c=0
        while i<j:
            r=nums[i]+nums[j]
            if r<target:
                c+=j-i
                i+=1
            else:
                j-=1
        return c
