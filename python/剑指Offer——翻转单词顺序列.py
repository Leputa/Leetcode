# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        return " ".join( [s for s in s.split(' ')[::-1]])

print(Solution().ReverseSentence('student. a am I'))