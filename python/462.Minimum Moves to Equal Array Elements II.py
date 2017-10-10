import math

class Solution(object):
	def minMoves2(self, nums):
		"""
        :type nums: List[int]
        :rtype: int
        """

		nums.sort()
		sum=0
		mid=nums[len(nums)//2]

		for i in nums:
			sum+=abs(i-mid)
		return sum