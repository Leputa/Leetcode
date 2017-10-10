import math

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ans=""
        for i in range (0,len(s),2*k):
        	if i==0:
        		ans+=s[i+k-1::-1]
        		ans+=s[i+k:i+2*k]

        	else:
        		ans+=s[i+k-1:i-1:-1]
        		ans+=s[i+k:i+2*k]
       	return ans

print(Solution().reverseStr("abcde",2))