class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead == None:
            return pHead

        head = ListNode(None)
        head.next = pHead

        preNode = head
        tmpNode = pHead

        while tmpNode != None:
            tag = 0
            val = tmpNode.val
            nextNode = tmpNode.next

            if nextNode == None:
                return head.next
            while nextNode.val == val:
                tag = 1
                nextNode = nextNode.next
                preNode.next = nextNode
                if nextNode == None:
                    return head.next
            if tag == 0:
                preNode = preNode.next
            tmpNode = preNode.next

        return head.next


if __name__ == '__main__':
    pHead = ListNode(1)
    tmpNode = pHead
    for i in [2, 3, 3, 4, 4, 5]:
        tmpNode.next = ListNode(i)
        tmpNode = tmpNode.next

    phead = Solution().deleteDuplication(pHead)
    while(phead!=None):
        print(phead.val)
        phead = phead.next



                


            





