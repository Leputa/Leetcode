# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        try:
            return int(s)
        except:
            return 0

print(Solution().StrToInt('1a33'))