class Solution:

    def __init__(self):
    	self.left=0
    	self.right=0
    	self.maxLength=-1

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        for i in range(len(s)):
        	self.extendLength(s,i,i)
        	self.extendLength(s,i,i+1)
        return s[self.left:self.right+1]


    def extendLength(self,s,i,j):
    	left,right=i,j
    	while(left>=0 and right<len(s)):
    		if s[left]!=s[right]:
    			break
    		else:
    			left-=1
    			right+=1

    	left+=1
    	right-=1

    	if right-left>self.maxLength:
    		self.maxLength=right-left
    		self.right=right
    		self.left=left



print(Solution().longestPalindrome("sdfasbaabdsfasdf"))


        