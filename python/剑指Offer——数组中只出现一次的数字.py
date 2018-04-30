class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        ans = []

        result = 0
        for num in array:
            result ^= num

        # 从右往左：记录第一个异或结果为1的位置，以此作为划分数组的依据
        # a,b两个数在某个位置不一样，才会异或结果为1 
        pos = 1

        while True:
            if result&1 == 1:
                break
            result = result >> 1 
            pos = pos << 1

        a,b = 0,0

        for num in array:
            if num&pos == 0:
                a ^= num
            else:
                b ^= num

        ans.extend([a,b])
        return ans


print(Solution().FindNumsAppearOnce([1,1,7,7,2,4]))





