class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        timeMinutes=[]
        for i in timePoints:
        	time=i.split(':')
        	minutes=int(time[0])*60+int(time[1])
        	timeMinutes.append(minutes)
        timeMinutes.sort()
        timeMinutes.append(timeMinutes[0]+24*60)

        min=24*60
        for i in range(1,len(timeMinutes)):
        	tmp=timeMinutes[i]-timeMinutes[i-1]
        	if(tmp<min):
        		min=tmp
        return min



print(Solution().findMinDifference(["23:59","00:09","20:10"]))