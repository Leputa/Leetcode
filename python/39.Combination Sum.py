class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res=[]
        tmpList=[]
        self.combine(0,candidates,target,tmpList,res)
        return res

    def combine(self,start,candidates,target,tmpList,res):
    	if target==0:
    		res.append(tmpList[:])
    		return
    	if target<0:
    		return 
    	for i in range(start,len(candidates)):
    		tmpList.append(candidates[i])
    		target-=candidates[i]
    		self.combine(i,candidates,target,tmpList,res)
    		target+=candidates[i]
    		tmpList.pop()


    		
print(Solution().combinationSum([2, 3, 7, 6],7))