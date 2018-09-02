# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None

        fastPtr, slowPtr = head, head
        while (fastPtr != None):
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next
            if fastPtr == None:
                return fastPtr
            fastPtr = fastPtr.next

            if slowPtr == fastPtr:
                break

        if fastPtr == None:
            return fastPtr


        fastPtr = head
        while (fastPtr != slowPtr):
            fastPtr = fastPtr.next
            slowPtr = slowPtr.next

        return fastPtr


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = head
    print(Solution().detectCycle(head))









