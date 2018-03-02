# -*- coding:utf-8 -*-

class MaxInnerRec:
    def countArea(self, A, n):
        stack=[]
        A.append(0)
        area=0
        i=0
        while(i<len(A)):
        	if len(stack)==0 or A[stack[len(stack)-1]]<=A[i]:
        		stack.append(i)
        	else:
        		h=A[stack.pop()]
        		if len(stack)==0:
        			area=max(area,h*i)
        		else:
        			area=max(area,h*(i-stack[len(stack)-1]-1))
        		i-=1
        	i+=1
        return area




print(MaxInnerRec().countArea([2,7,9,4,1],2))