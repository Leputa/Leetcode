import collections

# zero: Only digit with z
# two: Only digit with w
# four: Only digit with u
# six: Only digit with x
# eight: Only digit with g

class Solution:
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnts=collections.Counter(s)
        res=[]
        for x in '0eroz 6six 7evens 5fiev 8eihtg 4ourf 3treeh 2tow 1neo 9nnei'.split():   #拓补序列
        	res.append(x[0]*cnts[x[-1]])
        	for c in x:
        		cnts[c]-=cnts[x[-1]]
        return ''.join(sorted(res))



print(Solution().originalDigits("fviefuro"))