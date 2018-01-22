class Solution:
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """

        d.sort(key=lambda t:(-len(t),t))
        for i in range(len(d)):
        	word=d[i]
        	index=0
        	for k in range(len(word)):
        		tag=0
        		for j in range(index,len(s)):
        			if(s[j]==word[k]):
        				tag=1
        				index=j+1
        				if(k==len(word)-1):
        					return word
        				else:
        					break
        		if (tag==0):
        			break
        return ""

print(Solution().findLongestWord("bab", ["ba","ab","a","b"]))