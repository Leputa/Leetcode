class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        lenofNums=len(nums)
        while 0 in nums:
            nums.remove(0)
        while len(nums)<lenofNums:
        	nums.append(0)
    