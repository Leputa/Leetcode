# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        head = ListNode(None)

        while(pHead!=None):
            insertNode = pHead
            pHead = pHead.next

            insertNode.next = head.next
            head.next = insertNode
            
        return head.next

