import collections

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res=lo=hi=0
        counts=collections.Counter()
        for hi in range(1,len(s)+1):
        	counts[s[hi-1]] += 1
        	maxVal=counts.most_common(1)[0][1]
        	if hi-lo-maxVal>k:
        		counts[s[lo]]-=1
        		lo+=1
        return hi-lo

Solution().characterReplacement("AABABBA",1)        