class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        diff=0
        for i in nums:
        	diff^=i

        #if the single numbers are A and B
        #diff is A XOR B

        bitFlag=(diff&(~(diff-1))) #在 AXORB 中从右往左第一个为 1 的位，保留该位并将其他位置为 0 。

        ans=[0,0]

        for i in nums:
        	if((i&bitFlag)==0):
        		ans[0]^=i
        	else:
        		ans[1]^=i
        return ans




        