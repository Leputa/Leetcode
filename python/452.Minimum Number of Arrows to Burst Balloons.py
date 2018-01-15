class Solution:
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points=sorted(points,key=lambda x:x[1])
       	cnt=0
       	end=-9999999999999999999999
       	for i in range(len(points)):
       		if (points[i][0]>end):
       			cnt+=1
       			end=points[i][1]
       	return cnt




print(Solution().findMinArrowShots([[10,16], [2,8], [1,6], [7,12]]))