class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        r= []
        for i in nums:
            c= 0
            for j in nums:
                if j < i:
                     c+= 1
            r.append(c)
        return r
