class Solution(object):
    def lengthOfLIS_v1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = len(nums) * [0]
        for i in range(len(nums)):
            dp[i] = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        ret = 0
        for d in dp:
            if d > ret:
                ret = d
        return ret

    def getPosition(self, lis, num):
        low, high = 0, len(lis) - 1
        while(low < high):
            mid = (low + high) // 2
            if lis[mid] < num:
                low = mid + 1
            elif lis[mid] > num:
                high = mid - 1
            else:
                return mid
        


#上述解法效率过低


if __name__ == '__main__':
    print(Solution().lengthOfLIS_v1([10,9,2,5,3,7,101,18]))