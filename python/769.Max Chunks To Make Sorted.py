class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        length=[1]*len(arr)
        for i in range(len(arr)-1):
        	if max(arr[:i+1])<min(arr[i+1:]):
        		length[i]+=self.maxChunksToSorted(arr[i+1:])
       	return max(length)


print(Solution().maxChunksToSorted([1,0,2,3,4]))
