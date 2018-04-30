# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self,listNode):
        head = ListNode(None)

        while(listNode!=None):
            insertNode = listNode
            listNode = listNode.next

            insertNode.next = head.next
            head.next = insertNode
            
        return head.next

    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        listNode = self.reverseList(listNode)
        ans = []
        while(listNode != None):
            ans.append(listNode.val)
            listNode = listNode.next
        return ans


