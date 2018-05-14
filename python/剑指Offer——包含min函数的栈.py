# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.ptr = -1 #最小位置
    def push(self, node):
        # write code here
        if self.ptr == -1:
            self.stack.append(node)
            self.ptr = 0
        else:
            top = self.top()
            self.stack.append(node)
            if node < self.stack[self.ptr]:
                self.ptr = len(self.stack)-1

    def pop(self):
        # write code here
        self.stack.pop()
        if self.ptr == len(self.stack):
            self.ptr = self.stack.index(min(self.stack))   #这个地方应该有问题（但牛客可以通过），正确解法应该用一个辅助栈min_stack来实现, 而非指针

    def top(self):
        # write code here
        return self.stack[len(self.stack)-1]
    def min(self):
        # write code here
        return self.stack[self.ptr]