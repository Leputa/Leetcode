class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        max_num = -float("inf")
        sum_num = 0
        for i in range(len(nums)):
            sum_num += nums[i]
            if sum_num > max_num:
                max_num = sum_num
            if sum_num < 0:
                sum_num = 0
        return max_num