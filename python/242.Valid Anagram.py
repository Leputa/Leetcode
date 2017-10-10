class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
        	return False
        dic={}
        for i in s:
        	if dic.get(i,0)==0 :
        		dic[i]=1
        	else:
        		dic[i]+=1
        for i in t:
        	if dic.get(i,0)==0 :
        		return False
        	else:
        		dic[i]-=1
        return True