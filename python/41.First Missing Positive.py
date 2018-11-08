class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        while(i < len(nums)):
            if nums[i] <= 0 or nums[i] > len(nums) or nums[nums[i]-1] == nums[i]:
                i += 1
                continue
            tmp = nums[nums[i]-1]
            nums[nums[i]-1] = nums[i]
            nums[i] = tmp


        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1

        return len(nums) + 1



if __name__ == '__main__':
    print(Solution().firstMissingPositive([]))
