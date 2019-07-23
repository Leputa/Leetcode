from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        def swap(nums, i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
        for i in range(len(nums)):
            while nums[i] != i+1:
                if nums[i] != nums[nums[i]-1]:
                    swap(nums, i, nums[i]-1)
                else:
                    break
        ret = []
        for i in range(len(nums)):
            if nums[i] != i+1:
                ret.append(nums[i])
        return ret

if __name__ == "__main__":
    print(Solution().findDuplicates([4,3,2,7,8,2,3,1]))
