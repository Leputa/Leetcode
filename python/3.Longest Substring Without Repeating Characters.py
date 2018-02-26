# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         if len(s)==0 or len(s)==1:
#         	return len(s)
#         dic={}
#         ans=1
#         for i in range(len(s)):
#         	dic[s[i]]=i
#         	for j in range(i+1,len(s)):
#         		if j==len(s)-1:
#         			if dic.get(s[j],-1)>=i:
#         				ans=max(j-i,ans)
#         			else:
#         				ans=max(j-i+1,ans)
#         			return ans
#         		else:
#         			if dic.get(s[j],-1)>=i:
#         				ans=max(j-i,ans)
#         				dic.clear()
#         				break
#         			else:
#         				dic[s[j]]=j
#         return ans 

############## 上述解法超时 ################
 

class Solution:  
    # @return an integer  
    def lengthOfLongestSubstring(self, s):  
        start = maxLength = 0  
        usedChar = {}  
  
        for i in range(len(s)):  
            #if s[i] in usedChar and start <= usedChar[s[i]]:  
            if start <= usedChar.get(s[i],-1):
                start = usedChar[s[i]] + 1  
            else:  
                maxLength = max(maxLength, i - start + 1)  
  
            usedChar[s[i]] = i  
  
        return maxLength 




print(Solution().lengthOfLongestSubstring("pwwkew"))