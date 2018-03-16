class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)==0:
            return -1
        tag=-1
        left=0
        right=len(nums)-1
        if nums[left]<nums[right]:
            return self.binarySearch(nums,target)
        else:
            while(left<=right):
                mid=(left+right)//2
                if nums[mid]<nums[0]:
                    right=mid-1
                else:
                    left=mid+1
            tag=left
        if target == nums[0]:
            return 0
        elif target > nums[0]:
            return self.binarySearch(nums[:tag],target)
        else:
            if self.binarySearch(nums[tag:],target)==-1:
                return -1
            else:
                return (tag+self.binarySearch(nums[tag:],target))

    def binarySearch(self,nums,target):
        left=0
        right=len(nums)-1
        while(left<=right):
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
        return -1



print(Solution().search([4,5,6,7,8,1,2,3],8))