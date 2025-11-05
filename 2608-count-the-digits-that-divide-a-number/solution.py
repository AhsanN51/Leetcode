class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        z = str(num)
        k = 0
        for i in z:
            if num % int(i) == 0:
                k += 1
        return k
        
