class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
       	if a==b:
       		return -1
       	return self.max(len(a),len(b))

    def max(self,len1,len2):
    	if len1>=len2:
    		return len1
    	else :
    		return len2
