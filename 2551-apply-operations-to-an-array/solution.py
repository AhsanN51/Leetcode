class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2  
                nums[i + 1]= 0
        a=0
        for i in range(len(nums)): 
            if nums[i]!=0:
                nums[i],nums[a]=nums[a],nums[i]
                a+=1
        return nums
