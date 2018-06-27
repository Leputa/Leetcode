# -*- coding:utf-8 -*-

class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if len(num) == size:
            return [max(num)]
        if size == 0 or len(num)<size:
            return [] 
        q = []
        start = 0
        end = 0

        res = []
        i = 0
        while i < len(num):
            while (end-start < size):
                q.append(num[i])
                end += 1
                i += 1
            res.append(max(q[start:end]))
            q.append(num[i])
            start += 1
            end += 1
            i += 1

        res.append(max(q[start:end]))
        return res
