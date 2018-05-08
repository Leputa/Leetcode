# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 == None:
            return pHead2
        if pHead2 == None:
            return pHead1

        if pHead1.val < pHead2.val:
            head = pHead1
            pHead1 = pHead1.next
        else:
            head = pHead2
            pHead2 = pHead2.next

        tmpNode = head
        while (pHead1!=None and pHead2!=None):
            if pHead1.val<pHead2.val:
                tmpNode.next = pHead1
                pHead1 = pHead1.next
                tmpNode = tmpNode.next
            else:
                tmpNode.next = pHead2
                pHead2 = pHead2.next
                tmpNode = tmpNode.next

        if(pHead1!=None):
            tmpNode.next = pHead1
        if(pHead2!=None):
            tmpNode.next = pHead2

        return head
