# class Solution(object):
#     def numTrees(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         cnt = 0
#         return self.gen_count(1, n)

#     def gen_count(self, start, end):
#         if start > end:
#             return 0
#         if start == end:
#             return 1
#         cnt = 0
#         for i in range(start , end+1):
#             tagleft = self.gen_count(start, i-1)
#             tagright = self.gen_count(i+1, end)
#             if tagleft!=0 and tagright!= 0:
#                 cnt += tagleft*tagright
#             elif tagleft == 0 or tagright == 0:
#                 cnt += max(tagleft, tagright)
#         return cnt
#  递归直接超时了
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1 or n==0:
            return 1
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(0, i):
                dp[i] += dp[j] * dp[i-j-1]
        return dp[n]

print(Solution().numTrees(10)) 