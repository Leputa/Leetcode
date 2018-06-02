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
