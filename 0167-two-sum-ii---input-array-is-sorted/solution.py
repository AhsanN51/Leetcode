class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=numbers
        l=0
        r=len(numbers)-1
        while l<r:
            if n[l]+n[r]==target:
                return [l+1,r+1]
            elif n[l]+n[r]>target:
                r-=1
            else:
                l+=1
            
