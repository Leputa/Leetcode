class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if len(nums) == 0:
            return res
        nums.sort()
        res.append([])
        self.traceback(nums, res, [], 0)
        return res

    def traceback(self, nums, res, tmpList, pos):
        if pos == len(nums):
            return 
        
        i = pos
        while(i < len(nums)):
            tmpList.append(nums[i])
            res.append(tmpList[:])
            self.traceback(nums, res, tmpList, i+1)
            tmpList.pop()
            while(i+1 < len(nums) and nums[i] == nums[i+1]):
                i += 1
            i += 1











if __name__ == '__main__':
    print(Solution().subsetsWithDup([1,2,2]))