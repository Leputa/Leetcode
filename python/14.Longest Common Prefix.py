class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs==[]:
        	return ''
        else:
        	for i in range(1,len(strs)):
        		len1=len(strs[0])
        		len2=len(strs[i])
        		if len1>len2:
        			length=len2
        		else:
        			length=len1
        		strs[0]=strs[0][0:length]
        		for j in range(length):
        			if strs[0][j]!=strs[i][j]:
        				strs[0]=strs[0][0:j]
        				break
        	return strs[0]


