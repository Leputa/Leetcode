class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt=0
        for i in range(len(s)):
        	for j in range(i,len(s)):
        		if self.isPalindromic(s[i:j+1]):
        			#print(str(i)+"  "+str(j))
        			cnt+=1
        return cnt
    def isPalindromic(self,s):
    	return s==s[::-1]

Solution().countSubstrings("abc");