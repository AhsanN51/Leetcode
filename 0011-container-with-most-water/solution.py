class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        h=height
        i=0
        j=len(height)-1
        mn=0
        mxc=0
        a=0
        while i<j:
            mn=min(height[i],height[j])
            a=mn*(j-i)
            mxc=max(mxc,a)
            if h[j]>h[i]:
                i+=1
            else:
                j-=1
        return mxc
