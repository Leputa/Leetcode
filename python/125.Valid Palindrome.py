import string

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        copy1=s.replace(' ','')
        copy2=copy1
        for i in string.punctuation:
        	copy2=copy2.replace(i,'')
        copy3=copy2.lower()
        i=0
        j=len(copy3)-1
        while(i<=j):
        	if(copy3[i]!=copy3[j]):
        		return False
        	i+=1
        	j-=1
        return True


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
