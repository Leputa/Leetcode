# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if len(pushV)!=len(popV):
            return False

        stack = []
        i,j = 0,0
        while(i<len(pushV)):
            stack.append(pushV[i])
            i+=1
            while (len(stack)!=0 and stack[len(stack)-1]==popV[j]):
                stack.pop()
                j+=1
        if j == len(popV):
            return True
        else:
            return False


print(Solution().IsPopOrder([1,2,3,4,5],[4,3,5,1,2]))


