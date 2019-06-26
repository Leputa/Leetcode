class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[]
        if len(nums)<3:
        	return ans

        nums.sort()

        index=-1
        indexF=-1
        cnt=0
        for i in range(len(nums)):
        	if nums[i]==0:
        		cnt+=1
        		if indexF==-1:
        			indexF=i
        	if nums[i]>0:
        		index=i
        		break
        if cnt>=3:
        	ans.append([0,0,0])
        if index==-1:
        	return ans

        if indexF==-1:
        	indexF=index-1


        dic={}
       	for num in nums:
       		dic[num]=dic.get(num,0)+1


       	for i in range(len(nums[:indexF+1])):
       		if (nums[i]==nums[i-1]):
       			continue
       		for j in range(i+1,len(nums[:indexF+1])):
       			if (j!=i+1 and nums[j]==nums[j-1]):
       				continue
       			if(dic.get(-(nums[i]+nums[j]),0)!=0):
       				ans.append([nums[i],nums[j],-(nums[i]+nums[j])])

        for i in range(index,len(nums)):
        	if (nums[i]==nums[i-1]):
        		continue
        	for j in range(i+1,len(nums)):
        		if(j!=i+1 and nums[j]==nums[j-1]):
        			continue
        		if(dic.get(-(nums[i]+nums[j]),0)!=0):
        			ans.append([nums[i],nums[j],-(nums[i]+nums[j])])

       	return ans


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
      ret = []
      if len(nums) < 3:
        return ret

      nums = sorted(nums)

      dic = dict()
      for i in range(len(nums)):
        dic[nums[i]] = i
      i = 0
      while( i < len(nums) - 1):
        j = i + 1
        while ( j < len(nums)):
          t = - (nums[i] + nums[j])
          if dic.get(t) != None and dic[t] > j:
            ret.append([nums[i], nums[j], t])
            j = dic[nums[j]]
          i = dic[nums[i]] 
          j += 1
        i += 1

      return ret
       

print(Solution().threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))