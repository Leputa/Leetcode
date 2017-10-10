class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt=0
        ans=nums[0]
        for i in range(len(nums)):
        	if(nums[i]==ans):
        		cnt+=1
        	else:
        		cnt-=1
        		if(cnt<=0):
        			ans=nums[i]
        			cnt=0
        return ans

print(Solution().majorityElement([1,4,5,1,6,4,2,1,1,1,2,2,2,2,2,2,12,2,2,2,1,16,4,1]))