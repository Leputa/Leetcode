import itertools

cnt=0
class Solution(object):
    # def countArrangement(self, N):
    #     """
    #     :type N: int
    #     :rtype: int
    #     """
    #     if N==0:
    #     	return 1
    #     num=[]
    #     for i in range(N):
    #     	num.append(i+1)
        
    #     nums=list(itertools.permutations(num,N))

    #     cnt=0
    #     for i in range(len(nums)):
    #     	if self.isBeautifuArrangement(nums[i]):
    #     		cnt+=1
    #     return cnt


    # def isBeautifuArrangement(self,nums):
    # 	tag=0
    # 	for i in range(len(nums)): #The number at the ith position is divisible by i.
    # 		if nums[i]%(i+1)==0 or (i+1)%nums[i]==0:
    # 			continue
    # 		else:
    # 			return False
    # 	return True
    def countArrangement(self, N):
    	if N==0:
    		return 1
    	nums=[0]*(N+1)  #nums[i]表示有没有使用i(非下标），0没有，1有
    	self.getCount(N,1,nums)
    	return cnt

    def getCount(self,N,index,nums):
    	global cnt
    	if(index>N):
    		cnt+=1
    		return
    	for i in range(1,N+1):
    		#print (str(i)+"   "+str(nums[i]))
    		if(nums[i]==0 and (i%index==0 or index%i==0)):
    			nums[i]=1
    			self.getCount(N,index+1,nums)
    			nums[i]=0  #回溯

print(Solution().countArrangement(3))
        