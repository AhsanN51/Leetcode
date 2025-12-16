class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        a=len(nums)-1
        i = 0
        while i <= a:
            if nums[i]==val:
                nums[i],nums[a]=nums[a],nums[i]
                a-=1
            else :
                i+=1
        return a+1

