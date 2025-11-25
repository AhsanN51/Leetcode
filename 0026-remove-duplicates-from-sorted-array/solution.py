class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        start=0
        for i in range(1,n):
            if nums[i]!=nums[start]:
                nums[start+1]=nums[i]
                start+=1
        return start+1
