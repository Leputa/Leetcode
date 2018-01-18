# class Solution:
#     def __init__(self):
#     	self.ways=0
#     def findTargetSumWays(self, nums, S):
#         """
#         :type nums: List[int]
#         :type S: int
#         :rtype: int
#         """
#         self.dfs(0,nums,S)
#         return self.ways

#     def dfs(self,target,nums,S):
#     	if len(nums)==0:
#     		if(target==S):
#     			self.ways+=1
#     		return
#     	sumOfNums=sum(nums)
#     	if (sumOfNums+target<S or target-sumOfNums>S):
#     		return 
#     	self.dfs(target+nums[0],nums[1:],S)
#     	self.dfs(target-nums[0],nums[1:],S)
################ Time Limit Exceeded ##############


class Solution(object):
    def findTargetSumWays(self, nums, S):
    	dic={0:1}
    	for num in nums:
    		m={}
    		for key,val in dic.items():
    			m[key+num]=m.get(key+num,0)+val
    			m[key-num]=m.get(key-num,0)+val
    		dic=m
    	return dic.get(S,0)


print(Solution().findTargetSumWays([1],2))


