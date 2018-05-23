# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if ss == None or len(ss) == 0:
        	return ss

        ret = []
        tag = [0]*len(ss)
        self.getPermute(ret, '', ss, tag)
        return ret

    def getPermute(self, ret, tmpStr, ss, tag):
    	if len(tmpStr) == len(ss):
    		if tmpStr not in ret:
    			ret.append(tmpStr[:])
    			return 
    	for i in range(len(ss)):
    		if tag[i] == 0:
    			tag[i] = 1
    			tmpStr += ss[i]
    			self.getPermute(ret, tmpStr, ss, tag)
    			tmpStr = tmpStr[:-1]
    			tag[i] = 0
 #上述解法只能解决无重复字符的全排列




print(Solution().Permutation('aa'))

