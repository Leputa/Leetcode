class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        numK=self.findNumK(nums,k,0,len(nums)-1)
        return numK


    def findNumK(self,nums,k,left,right):
    	pivot=nums[left]
    	cnt=0
    	i=left+1
    	j=right
    	while(i<=j):
    		while(i<=j and nums[i]>=pivot):
    			i+=1
    			cnt+=1
    		while(i<=j and nums[j]<pivot):
    			j-=1
    		if(i<=j):
    			nums[i],nums[j]=nums[j],nums[i]
    			i+=1
    			j-=1
    			cnt+=1
    	nums[left],nums[j]=nums[j],nums[left]
    	if cnt==k-1:
    		return pivot
    	elif(cnt<k-1):
    		return self.findNumK(nums,k-cnt-1,j+1,right)
    	else:
    		return self.findNumK(nums,k,left,j-1)


print(Solution().findKthLargest([3,2,1,5,6,4,6,6],9))
        