class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """ 
        ret = []
        ret.append(S[:])
        self.traceback(S, ret, 0)
        return ret
    

    def traceback(self, S, ret, start):
    	for i in range(start, len(S)):
    		if (S[i] >= 'a' and S[i] <= 'z'):
    			S = S[:i] + S[i].upper() + S[i+1:]
    			ret.append(S[:])
    			self.traceback(S, ret, i+1) 
    			S = S[:i] + S[i].lower() + S[i+1:] 
    		elif (S[i] >= 'A' and S[i] <= 'Z'):
    			S = S[:i] + S[i].lower() + S[i+1:]
    			ret.append(S[:])
    			self.traceback(S, ret, i+1)
    			S = S[:i] + S[i].upper() + S[i+1:]



