class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans=''
        tmp=''
        for i in s :
        	if i!=' ':
        		tmp+=i
        	else:
        		tmp=tmp[::-1]
        		ans+=tmp
        		ans+=' '
        		tmp=''
        tmp=tmp[::-1]
        ans+=tmp
        return ans


print(Solution().reverseWords("Let's take LeetCode contest"))
