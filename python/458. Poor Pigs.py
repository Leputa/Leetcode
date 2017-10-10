class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        unit=minutesToTest//minutesToDie+1
        pig=0
        while(unit**pig<buckets):
        	pig+=1
        return pig

print(Solution().poorPigs(1000,15,60))