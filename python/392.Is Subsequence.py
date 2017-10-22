class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if(len(s)==0 and len(t)==0):
        	return True
        if(len(t)==0):
        	return False
        j=0
        i=0
        while (i<len(s)):
        	if(s[i]==t[j]):
        		i+=1
        		j+=1
        	else:
        		j+=1
        	if(i==len(s)):
        		return True
        	if(j==len(t)):
        		return False
        return True

print(Solution().isSubsequence("abc","ahbgdc"))

        

