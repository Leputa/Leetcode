# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence) == 0:
            return False
        if len(sequence) <= 1:
            return True
        return self.splitTree(sequence)
        
    def splitTree(self, sequence):
        if len(sequence) <= 1:
            return True
        root = sequence[-1]
        split_idx = -1
        for i in range(len(sequence)):
            if sequence[i] > root:
                split_idx = i
                break
        if split_idx == -1:   # 全部比root小
            split_idx = len(sequence)-1
        for i in range(split_idx, len(sequence)):
            if sequence[i] < root:
                return False
        return self.splitTree(sequence[:split_idx]) and self.splitTree(sequence[split_idx:len(sequence)-1])


print(Solution().VerifySquenceOfBST([4,8,6,12,16,14,10]))
