class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=0
        nums=set(nums)
        l=len(nums)
        if 0 in nums:
            return l-1
        else:
            return l
