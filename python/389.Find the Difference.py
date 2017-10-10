class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for i in t :
            if (s+t).count(i)%2:
            	return i
        

