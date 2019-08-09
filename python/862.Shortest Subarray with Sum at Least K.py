from collections import deque

class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        frontSum = [0] * (len(A) + 1)
        for i in range(1, len(A)+1):
            frontSum[i] = frontSum[i-1] + A[i-1]
        q = deque()
        ret = -1
        for i in range(len(A)+1):
            while(len(q) != 0 and frontSum[i] - q[-1] <= 0):
                q.pop()
            while(len(q) != 0 and frontSum[i] - q[0] >= K):
                j = q.popleft()
                length = j - i
                if ret == -1:
                    ret = length
                elif length < ret:
                    ret = length
            q.append(i)
        return ret


