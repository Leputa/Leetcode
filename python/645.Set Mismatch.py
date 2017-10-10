class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        list=[]
        dict={}
        sum=0
        min=10005
        max=0
        for i in nums:
        	sum=sum+i
        	if(i>max):
        		max=i
        	if(i<min):
        		min=i
        	if dict.get(i,0)==1:
        		list.append(i)
        	else:
        		dict[i]=1
        if (min!=1):
        	tmp=1
        elif(list[0]==max):
        	tmp=max+1
        else:
        	tmp=(1+max)*len(nums)//2-(sum-list[0])
        list.append(tmp)
        return list

print(Solution().findErrorNums([1,2,2,4]))