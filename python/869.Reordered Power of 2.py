import math

class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        unique_replace = self.transform(N)
        for i in range(32):
            if self.transform(2**i) == unique_replace:
                return True
        return False

    def transform(self, N):
        ret = 0
        while N > 0:
            ret += math.pow(10, N%10)
            N //= 10
        return ret

print(Solution().reorderedPowerOf2(46))