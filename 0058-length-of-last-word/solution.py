class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.strip()
        j=len(s)-1
        print(s)
        while j>=0:
            if s[j]==" ":
                break
            j-=1
        return len(s[j+1:len(s)])
