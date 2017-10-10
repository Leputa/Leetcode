class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        '''
        if (len(nums)==0):
        	return False
        dic={}
        for i in nums:
        	if dic.get(i,0)==0:
        		dic[i]=1
        	else:
        		dic[i]+=1
        for i in dic:
        	if dic[i]<2:
        		return False
        return True
        '''
        if (len(nums)==0):
        	return False
        numscopy=set(nums)
        return not len(numscopy)==len(nums)

Solution().containsDuplicate([1212121212])
print(354989075909990+712982900)