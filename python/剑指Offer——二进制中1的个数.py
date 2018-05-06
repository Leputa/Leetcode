# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        cnt = 0
        pos = 1
        while(pos<(1<<32)): #32位是根据其他语言int默认4byte猜的
            if (n&pos)!=0:
                cnt += 1
            pos=pos<<1      #python和其他语言这儿有点不一样
        return cnt

print(Solution().NumberOf1(-1))
