class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[]
        ans.append([])
        self.dfs(ans,nums,[])
        return ans

    def dfs(self,ans,nums,tmpList):
    	if(len(nums)==0):
    		return
    	newtmpList1=tmpList[:]
    	self.dfs(ans,nums[1:],newtmpList1)
    	newtmpList2=tmpList[:]
    	newtmpList2.append(nums[0])
    	ans.append(newtmpList2)
    	self.dfs(ans,nums[1:],newtmpList2)

print(Solution().subsets([1,2,3]))