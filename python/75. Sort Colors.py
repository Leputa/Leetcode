from typing import List

class Solution:
    def swap(self, nums, i, j):
        print(i, j)
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt_0, cnt_1, cnt_2 = 0, 0, 0
        for num in nums:
            if num == 0:
                cnt_0 += 1
            if num == 1:
                cnt_1 += 1
            if num == 2:
                cnt_2 += 1

        for i in range(len(nums)):
            if i < cnt_0:
                nums[i] = 0
            elif i >= cnt_0 and i < cnt_0 + cnt_1:
                nums[i] = 1
            else:
                nums[i] = 2




if __name__ == "__main__":
    Solution().sortColors([2,0,2,1,1,0])


