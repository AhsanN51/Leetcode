class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        fds={}
        for i in s:
            if i in fds:
                fds[i]+=1
            else:
                fds[i]=1
        fdt={}
        for i in t:
            if i in fdt:
                fdt[i]+=1
            else:
                fdt[i]=1
        if len(fds)!=len(fdt):
            return False
        if fds==fdt:
            return True
        else:
            return False
