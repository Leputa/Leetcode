class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num<=9:
        	return num
        ans=num%9
        if ans==0:
        	return 9
        else :
        	return ans