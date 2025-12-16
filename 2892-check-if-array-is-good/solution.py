class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n =len(set(nums))
        if (n+1)!=len(nums):
            return False
        for i in range(len(nums)):
            if (i+1) not in nums and (i+1)!=(n+1):
                return False
            elif nums[i]!=n:
                if nums.count(nums[i])!=1:
                    return False
            else:
                if nums.count(n)!=2:
                    return False
        return True    
