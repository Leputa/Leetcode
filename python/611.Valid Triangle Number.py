class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ans=0
        for i in range(len(nums)-2):
        	j=i+1;k=i+2
        	while(k<len(nums)):
        		while(j<k and nums[i]+nums[j]<=nums[k]):
        			j+=1
        		ans=ans+k-j
        		k+=1
        return ans

print(Solution().triangleNumber([2,7,6,5,4]))