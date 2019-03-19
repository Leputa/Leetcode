class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        dp = dict()
        s = set(A)
        for i in range(len(A)-1):
            for j in range(i+1, len(A)):
                dp[(A[i], A[j])] = 2
                if A[j] - A[i] in s and dp.get((A[j]-A[i], A[i])) != None:
                    dp[(A[i], A[j])] = dp[(A[j]-A[i], A[i])] + 1
        ret = max(dp.values())
        return ret if ret > 2 else 0