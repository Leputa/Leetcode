import collections

class Solution:
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        count={}
        count[0]=-1                       #考虑0倍的情景
        sumSub=0
        for i in range(len(nums)):
        	sumSub+=nums[i]
        	if k!=0:
        		sumSub%=k                 #(a+b)%k==(a%k+b)%k
        	if(count.get(sumSub)!=None):
        		if (i-count[sumSub]>1):
        			return True
        	else:
        		count[sumSub]=i
        return False

print(Solution().checkSubarraySum([0,0,5],2))