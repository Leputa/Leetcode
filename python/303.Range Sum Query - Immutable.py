class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.dp=[]
        sum=0
        self.dp.append(0)
        for i in range(len(nums)):
            sum+=nums[i]
            self.dp.append(sum)
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.dp[j+1]-self.dp[i]
       
     


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)