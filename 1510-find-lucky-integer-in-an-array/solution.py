class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        mx=-1
        for i in arr:
            if arr.count(i)==i and i>mx:
                mx=i
        return mx

