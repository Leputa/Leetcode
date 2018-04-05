class Solution:
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        s = s.strip()

        sign = -1 if s[0] =='-' else 1
        if s[0] in ['-','+']:
            s=s[1:]
        ret,i = 0,0
        while i<len(s) and s[i].isdigit():
            ret = ret * 10 + ord(s[i]) - ord('0')
            i +=1

        return max(min(sign*ret,2147483647),-2147483648)

        