import random

class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums=nums
        
    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        ans=[]
        for i in range(len(self.nums)):
        	if(self.nums[i]==target):
        		ans.append(i)
        if (len(ans)==0):
        	return -1
        return ans[random.randint(0,len(ans)-1)]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)