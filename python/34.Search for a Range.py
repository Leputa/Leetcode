class Solution:

    def midSearch(self,nums,target):
        left = 0
        right = len(nums)-1
        while (left <= right):
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return -1

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mid = self.midSearch(nums,target)
        if mid == -1:
            return [-1,-1]
        
        right = mid
        left = mid

        tmpRight = right
        tmpLeft = left

        while (tmpRight < len(nums)):
            tmpRight = self.midSearch(nums[right+1:],target)
            if tmpRight == -1:
                break
            right += tmpRight + 1
        while (tmpLeft >= 0):
            tmpLeft = self.midSearch(nums[:left],target)
            if tmpLeft == -1:
                break
            left = tmpLeft
        
        return [left,right]

print(Solution().searchRange([5,7,7,8,8,8,8,8,10],8))