class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }

        if s == None or len(s) == 0:
            return 0
        if len(s) == 1:
            return dic[s[0]]
        
        tag = 0
        rnt = 0
        for i in range(len(s)-1):
            if dic[s[i]] > dic[s[i+1]]:
                rnt += dic[s[i]]
                tag = 0
            elif dic[s[i]] < dic[s[i+1]]:
                rnt -= dic[s[i]]
                tag = 1
            else:
                if tag == 0:
                    rnt += dic[s[i]]
                else:
                    rnt -= dic[s[i]]

        rnt += dic[s[len(s) - 1]]
        
        return rnt


print(Solution().romanToInt("MCMXCIV"))
        
