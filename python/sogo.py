'''
一个背包容量90，一堆items体积[0, 1, 2...90], 现选10个items填满背包，可以重复选，有多少种选法 
eg: 0, 0, 0, 0, 0, 0, 0, 0, 90
'''

def dp_bags(volume, items, nums):
    #dp[i][j] 使用了i个格子，容量为j的背包的装载数量
    dp = [[0] * (volume + 1) for i in range(len(items)+1)]
    for i in range(len(items)+1):
        dp[i][0] = 1
    for i in range(1, len(items) + 1):
        for j in range(1, volume + 1):
            for item in items:
                if j >= item:
                    dp[i][j] += dp[i-1][j-item]
    """
    我觉得这样写有重复：
    比如[0, 0, 0, 0, 0, 0, 0, 0, 90]
       [90, 0, 0, 0, 0, 0, 0, 0, 0]
    会算两种...
    """
    return dp[len(items)][volume]


global cnt
cnt = 0

def bags(volume, items, nums):
    '''
    时间复杂度太大了，跑不出来
    '''
    global cnt 
    dfs(volume, items, nums)
    return cnt
    

def dfs(volume, items, nums):
    if nums == 0 and volume == 0:
        global cnt 
        cnt += 1
        return 

    for item in items:
        if nums == 1:
            if item == volume:
                dfs(volume-item, items, nums-1)
                return
        else:
            if item < volume:
                dfs(volume-item, items, nums-1)
            else:
                return 


if __name__ == "__main__":
    volume = 90
    nums = 10
    items = [i for i in range(0, 91)]
    print(dp_bags(volume, items, nums))