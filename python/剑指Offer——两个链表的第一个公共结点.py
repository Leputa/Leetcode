# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        cnt1 = self.getLength(pHead1)
        cnt2 = self.getLength(pHead2)

        if cnt1 > cnt2:
            for i in range(cnt1 - cnt2):
                pHead1 = pHead1.next
        else:
            for i in range(cnt2 - cnt1):
                pHead2 = pHead2.next

        while pHead1 != None:
            if pHead1 == pHead2:
                return pHead1
            pHead1 = pHead1.next
            pHead2 = pHead2.next


    def getLength(self, pHead):
        cnt = 0
        tmpNode = pHead
        while tmpNode != None:
            cnt += 1
            tmpNode = tmpNode.next
        return cnt 