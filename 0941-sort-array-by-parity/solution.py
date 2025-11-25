class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counter=0
        for i in range(0,len(nums)):
            if nums[i]%2==0:
                t=nums[i]
                nums[i]=nums[counter]
                nums[counter]=t
                counter+=1
        return nums
