class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dic = {}
        for i in range(len(s)-10+1):
        	sub_string = s[i:i+10]
        	dic[sub_string] = dic.get(sub_string, 0) + 1
        res = []
        for key,values in dic.items():
        	if values > 1:
        		res.append(key)
        return res

if __name__ == '__main__':
	print(Solution().findRepeatedDnaSequences("AAAAAAAAAAA"))
