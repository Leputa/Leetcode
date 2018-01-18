class Solution:
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if (words==None or len(words)==0):
        	return 0
        value=[0]*len(words)
        for i in range(len(words)):
        	word=words[i]
        	for j in range(len(word)):
        		value[i]=value[i]|(1<<(ord(word[j])-ord('a')))
        max=0
        for i in range(len(words)):
        	for j in range(1,len(words)):
        		if((value[i]&value[j])==0 and len(words[i])*len(words[j])>max):
        			max=len(words[i])*len(words[j])
       	return max


print(Solution().maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))