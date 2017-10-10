import math

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        sum=0
        cnt=0
        tag=0
        length=len(flowerbed)
        for i in range(length):
        	if tag==0:
        		if flowerbed[i]==0:
        			cnt+=1
        			if i==length-1:
        				sum+=math.ceil(cnt/2)
        		else:
        			sum+=cnt//2
        			cnt=0
        			tag=1
        	else:
        		if flowerbed[i]==0:
        			cnt+=1
        			if i==length-1:
        				sum+=cnt//2
        		else:
        			if cnt%2==0:
        				sum+=cnt/2-1
        			else:
        				sum+=cnt//2
        			cnt=0
        	if(sum>=n):
        		return True
        return False

print(Solution().canPlaceFlowers([0,0,0,0,0],3))
