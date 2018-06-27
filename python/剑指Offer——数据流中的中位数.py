# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.list = []

    def Insert(self, num):
        # write code here
        for i in range(len(self.list)):
            if num < self.list[i]:
                self.list.insert(i, num)
                return 
        self.list.append(num)
    
    def GetMedian(self):
        # write code here
        length = len(self.list)
        if length%2 == 0:
            return (self.list[length//2] + self.list[length//2 -1])/2.0
        else:
            return self.list[length//2]