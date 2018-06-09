# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        return (s + s)[n: n+len(s)]

print(Solution().LeftRotateString('abcXYZdef', 3))