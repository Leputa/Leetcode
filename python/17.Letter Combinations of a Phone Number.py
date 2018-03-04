class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ans=[]
        if len(digits)==0:
        	return ans

        dic = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        tmpList=[]
       	self.Combination(digits,ans,tmpList,dic)
       	return ans

    def Combination(self,digits,ans,tmpList,dic):
    	if len(digits)==0:
    		ans.append(''.join(tmpList.copy()))
    		return
    	string=dic[digits[0]]
    	for j in range(len(string)):
    		tmpList.append(string[j])
    		self.Combination(digits[1:],ans,tmpList,dic)
    		tmpList.pop()

print(Solution().letterCombinations("45"))















