class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        fd1={}
        for v in strs:
            isorted=''.join(sorted(v))
            if isorted in fd1:
                fd1[isorted].append(v)
            else:
                fd1[isorted]=[v]
        return list(fd1.values())
