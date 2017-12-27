class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[]
        tag=[False]*len(nums)
        self.getPermute(nums,ans,[],tag)
        return ans
    
    def getPermute(self,nums,ans,tmpList,tag):
    	if(len(tmpList)==len(nums)):
    		ans.append(tmpList[:])
    		return
    	for i in range(len(nums)):
    		if(not tag[i]):
    			tag[i]=True
    			tmpList.append(nums[i])
    			self.getPermute(nums,ans,tmpList,tag)
    			#回溯
    			tmpList.pop()
    			tag[i]=False


print(Solution().permute([1,2,3]))