

def getMaxSum(nums):
    '''
    区间dp
    dp[i][j] = nums[i] ~ nums[j]可以多赢的分数
    '''
    dp = [[0] * len(nums) for _ in range(len(nums))]
    for i in range(len(nums)):
        dp[i][i] = nums[i]
    for dis in range(1, len(nums)):
        for i in range(len(nums)-dis):
            dp[i][i+dis] = max(nums[i] - dp[i+1][i+dis], nums[i+dis]-dp[i][i+dis-1])

    return (sum(nums) - dp[0][len(nums)-1]) // 2 + dp[0][len(nums)-1]

if __name__ == "__main__":
    # print(sumLessThanK([-2, 0, 1, 2, 3, 6], 2))
    n = int(input())
    nums = list(map(int, input().split(" ")))
    print(getMaxSum(nums))