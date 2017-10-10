class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        cntLevel=0
        cntVertical=0

        for i in moves:
        	if i=='U':
        		cntVertical+=1
        	elif i=='D':
        		cntVertical-=1
        	elif i=='R':
        		cntLevel+=1
        	else :
        		cntLevel-=1
        return cntLevel==0 and cntVertical==0

