WA="a"
class Solution(object):
    def kthCharacter(self, k,wc=WA):
        """
        :type k: int
        :rtype: str
        w = WA
        wc = w
        while len(wc) <= k:
            empty = ""
            for i in wc:
                empty += chr(int(ord(i)) + 1)
            wc = wc + empty
        return wc[k - 1]
        """
        if len(wc) > k:
            return wc[k - 1]
        else:
            empty = ""
            for i in wc:
                empty += chr(ord(i) + 1)
            new_wc = wc + empty
            return self.kthCharacter(k, new_wc)

