# -*- coding:utf-8 -*-

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if pHead == None:
            return None
        
        oldNode = pHead
        newPreNode = None
        nHead = None
        dic = {}
        old_to_new = {}

        while (oldNode!=None):

            newNode = RandomListNode(oldNode.label)
            newNode.random = oldNode.random

            old_to_new[id(oldNode)] = id(newNode)
            dic[id(newNode)] = newNode
            oldNode = oldNode.next

            if newPreNode == None:
                newPreNode = newNode
                nHead = newNode
            else:
                newPreNode.next = newNode
                newPreNode = newPreNode.next

        newPreNode = nHead
        while newPreNode!=None:
            if newPreNode.random != None:
                newPreNode.random = dic[old_to_new[id(newPreNode.random)]]      #random由指向old改为指向new
            newPreNode = newPreNode.next
        
        return nHead



        

