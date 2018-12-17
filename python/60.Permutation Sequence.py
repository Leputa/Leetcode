# class Solution(object):
#     def __init__(self):
#         self.idx = 0
#         self.ans = []
#     def getPermutation(self, n, k):
#         """
#         :type n: int
#         :type k: int
#         :rtype: str
#         """
#         ans = []
#         tag = [False] * n
#         self.traceBack(ans, tag, k, n)
#         return "".join(str(a) for a in self.ans)

#     def traceBack(self, ans, tag, k, n):
#         for i in range(1, n+1):
#             if not tag[i-1]:
#                 tag[i-1] = True
#                 ans.append(i)
#                 if len(ans) == n:
#                     self.idx += 1
#                     if self.idx == k:
#                         self.ans = ans[:]
#                         return 
#                 self.traceBack(ans, tag, k, n)
#                 ans.pop()
#                 tag[i-1] = False


# print(Solution().getPermutation(9, 171669))

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        k -= 1
        nums = [i for i in range(1, n+1)]

        # (n-1)! 
        factorial = 1
        for i in range(2, n):
            factorial *= i
        
        ans = []
        round = n-1
        while(round >= 0):
            index = k // factorial
            ans.append(nums[index])
            nums.pop(index)

            k %= factorial
            if round > 0:
                factorial //= round
            round -= 1
        return "".join(str(a) for a in ans)

print(Solution().getPermutation(9, 171669))

