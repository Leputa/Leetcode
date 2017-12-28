# class Solution(object):
#     def __init__(self):
#     	self.longest=0
#     def arrayNesting(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         tag=[False]*len(nums)
#         S=[]
#         self.getArrayNesting(nums,tag,S)
#         return self.longest

#     def getArrayNesting(self,nums,tag,S):
#     	if(len(S)==len(nums)):
#     		return
#     	for i in range(len(nums)):
#     		if(tag[i]==False):
#     			tag[i]=True
#     			if(len(S)==0):
#     				S.append(i)
#     				if(len(S)>self.longest):
#     					self.longest=len(S)
#     				self.getArrayNesting(nums,tag,S)
#     				S.pop()
#     			else:
#     				tail=S[len(S)-1]
#     				if(nums[tail]==i):
#     					S.append(i)
#     					if(len(S)>self.longest):
#     						self.longest=len(S)
#     					self.getArrayNesting(nums,tag,S)
#     					S.pop()
#     			tag[i]=False

# print(Solution().arrayNesting([5,4,0,3,1,6,2]))
# 上述方法超时了

#从多个起点到达同一个值之后的路径都是完全相同的，所以每个值最多遍历一次
class Solution:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSize=0
        for i in range(len(nums)):
        	size=0
        	index=i
        	while(nums[index]>=0):
        		nextIndex=nums[index]
        		nums[index]=-1
        		index=nextIndex
        		size+=1
        	if size>maxSize:
        		maxSize=size
        return maxSize

