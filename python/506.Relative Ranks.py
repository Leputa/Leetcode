


class Solution(object):

    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        numscopy=nums[:]
        numscopy.sort(reverse=True)
        dic={}
        for i in range(len(numscopy)):
            dic[numscopy[i]]=i
        ans=[]
        for i in nums:
            if dic[i]==0:
               ans.append("Gold Medal")
            elif dic[i]==1:
               ans.append("Silver Medal")
            elif dic[i]==2:
                ans.append("Bronze Medal")
            else:
                ans.append(str(dic[i]+1))
        return ans


print(Solution().findRelativeRanks([5,12,8,6,1,3,2]))
