class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        ta=0
        tc=0
        for a in apple:
            ta+=a
        for c in capacity:
            tc+=c
        if ta==tc:
            return len(capacity)
        ct=0
        c=capacity
        while ta>0:
            mx=max(c)
            ta-=mx
            c.pop(c.index(mx))
            ct+=1
        return ct

