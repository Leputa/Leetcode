class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        if n == 1:
            return 1

        numbers = [1]
        i2, i3, i5 = 0, 0, 0
        for i in range(n-1):
            n2, n3, n5 = numbers[i2]*2, numbers[i3]*3, numbers[i5]*5
            minNum = min(n2, n3, n5)
            numbers.append(minNum)
            i2 += minNum == n2
            i3 += minNum == n3
            i5 += minNum == n5
        return minNum


class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        i2, i3, i5 = 0, 0, 0 
        nums = [1]
        for i in range(1, index):
            num2 = nums[i2] * 2
            num3 = nums[i3] * 3
            num5 = nums[i5] * 5
            ugly_num = min(num2, num3, num5)
            nums.append(ugly_num)
            if ugly_num == num2:
                i2 += 1
            if ugly_num == num3:
                i3 += 1
            if ugly_num == num5:
                i5 += 1
        return nums[-1]


if __name__ == "__main__":
    print(Solution().GetUglyNumber_Solution(7))
