class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        if n <= 0:
            return 0
        if n == 1:
            return 1

        primeIndex = [0]*len(primes)
        tmpUglyNumber = [0]*len(primes)
        numbers = [1]

        for i in range(n-1):
            for j in range(len(tmpUglyNumber)):
                tmpUglyNumber[j] = numbers[primeIndex[j]] * primes[j]
            minNum = min(tmpUglyNumber)
            numbers.append(minNum)
            for j in range(len(primeIndex)):
                primeIndex[j] += minNum == tmpUglyNumber[j]

        return minNum


print(Solution().nthSuperUglyNumber(12, [2,7,13,19]))

