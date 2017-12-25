class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        copy=nums[:]
        for i in nums:
        	copy.append(i)
        # nums=copy[n-k:2*n-k]
        for i in range(n):
        	nums[i]=copy[n-k+i]
 
Solution().rotate([1,2,3,4,5,6,7],3) 