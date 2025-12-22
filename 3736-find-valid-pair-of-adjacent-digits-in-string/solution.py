class Solution(object):
    def findValidPair(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=list(s)
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in range(len(s)-1):
            if s[i]!=s[i+1] and int(s[i])==d[s[i]] and int(s[i+1])==d[s[i+1]]:
                return str(s[i]+s[i+1])
        return ""
