# -*- coding:utf-8 -*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        quick_ptr = pHead
        slow_ptr = pHead

        while (quick_ptr!=None and slow_ptr!=None):
            try:
                quick_ptr = quick_ptr.next.next
                slow_ptr = slow_ptr.next
            except:
                return None
            
            if quick_ptr == slow_ptr:
                quick_ptr = pHead

                while(quick_ptr != slow_ptr):
                    quick_ptr = quick_ptr.next
                    slow_ptr = slow_ptr.next
                return quick_ptr

        return None

