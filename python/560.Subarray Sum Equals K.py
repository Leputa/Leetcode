# class Solution:
#     def subarraySum(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         nums.append(0)
#         start=-1
#         end=0
#         sumSub=nums[end]
#         ans=0
#         while(end<len(nums)-1 and start<len(nums)-1):
#         	if start==end:
#         		end+=1
#         		sumSub+=nums[end]
#         		continue
#         	if(sumSub==k):
#         		ans+=1
#         		end+=1
#         		sumSub+=nums[end]
#         	elif(sumSub>k):
#         		start+=1
#         		sumSub-=nums[start]
#         	else:
#         		end+=1
#         		sumSub+=nums[end]
#         return ans

# print(Solution().subarraySum([-1,-1,1],1))
# 上述解法没考虑负数

# class Solution:
#     def subarraySum(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         sumSub=[0]*(len(nums)+1)
#         ans=0
#         for i in range(len(nums)):
#         	sumSub[i+1]=sumSub[i]+nums[i]
#         for i in range(len(nums)):
#         	for j in range(i+1,len(nums)+1):
#         		if sumSub[j]-sumSub[i]==k:
#         			ans+=1
#         return ans

# print(Solution().subarraySum([-1,-1,1],0))
# 上述解法超时

import collections

class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count=collections.Counter()
        count[0]=1
        ans=sumSub=0
        for num in nums:
        	sumSub+=num
        	ans+=count[sumSub-k]
        	count[sumSub]+=1
        return ans

print(Solution().subarraySum([-1,-1,1],0))