from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        swap_pos = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                swap_pos = i
                break
        
        if swap_pos == -1:
            nums =  self.reverse(nums, 0, len(nums)-1)
            return 
        
        for i in range(len(nums)-1, swap_pos, -1):
            if nums[i] > nums[swap_pos]:
                self.swap(nums, i, swap_pos)
                break
        
        self.reverse(nums, swap_pos+1, len(nums)-1)
        
    def reverse(self, nums, left, right):
        while(left < right):
            self.swap(nums, left, right)
            left += 1
            right -= 1

    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp