class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=0
        p=1
        k=n
        while k>0:
            d=k%10
            s+=d
            p*=d
            k//=10
        return p-s
