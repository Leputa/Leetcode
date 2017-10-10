import sys
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=0
        minNum=sys.maxsize
        for i in nums:
        	sum+=i
        	if i <minNum:
        		minNum=i
        return (sum-minNum*len(nums))




        