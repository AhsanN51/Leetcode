class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p=max(nums)
        curmax=curmin=1
        for n in nums:
            temp=curmax*n
            curmax=max(temp,curmin*n,n)
            curmin=min(temp,curmin*n,n)
            p=max(p,curmax)
        return p
