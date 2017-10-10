class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cnt=0
        # for i in range(len(nums)-1):
        #     if(nums[i]>nums[i+1]):
        #         if(i!=0 and nums[i-1]>nums[i+1]):
        #             return False
        #         cnt+=1
        #     if cnt>1:
        #         return False
        # return True
        max=-214809800
        list=[]
        for i in range(len(nums)):
            if(nums[i]>=max):
                max=nums[i]
            else:
                tag=0
                for j in range(i):
                    if tag==1:
                        break
                    if j not in list and nums[i]<nums[j]:
                        cnt+=1
                        list.append(j)
                        tag=1
                    if cnt==2:
                        return False
        return True



print(Solution().checkPossibility([1,5,4,6,7,10,8,9]))