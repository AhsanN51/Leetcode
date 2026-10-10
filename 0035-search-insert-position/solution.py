class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l=0
        r=len(nums)-1
        m=0
        while l<=r:
            m=(l+r)//2
           # print(m)
            if nums[m]==target:
                return m
            elif nums[m]<target:
                #print("left")
                l=m+1
            else:
                #print("right")
                r=m-1
        return r+1
