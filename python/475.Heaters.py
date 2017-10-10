class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        j=0
        res=0
        tmp=0
        for i in range(len(houses)):
        	while j<len(heaters) and houses[i]>heaters[j]:
        		j+=1
        	if(j==len(heaters)):
        		tmp=houses[i]-heaters[j-1]
        	elif(j==0):
        		tmp=heaters[j]-houses[i]
        	elif(heaters[j]>houses[i]):
        		tmp=min(heaters[j]-houses[i],houses[i]-heaters[j-1])
        	if tmp>res:
        		res=tmp
        return res


