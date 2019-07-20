# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        h = ListNode(None)
        h.next = head
        return self.merge_Sort(h).next

    def merge_Sort(self, head):
        if head == None or head.next == None or head.next.next == None:
            return head
        
        # 切分链表
        slow_ptr = head
        quick_ptr = head
        while(quick_ptr != None and quick_ptr.next != None):
            slow_ptr = slow_ptr.next
            quick_ptr = quick_ptr.next.next
        
        head2 = ListNode(None)
        head2.next = slow_ptr.next
        slow_ptr.next = None
        
        head = self.merge_Sort(head)
        head2 = self.merge_Sort(head2)
        head = self.merge(head, head2)
        return head

    def merge(self, head1, head2):
        preNode = head1
        tmpNode1 = head1.next
        tmpNode2 = head2.next

        while(tmpNode1 != None and tmpNode2 != None):
            if tmpNode1.val < tmpNode2.val:
                tmpNode1 = tmpNode1.next
            else:
                head2.next = tmpNode2.next
                preNode.next = tmpNode2
                tmpNode2.next = tmpNode1
                tmpNode2 = head2.next
            preNode = preNode.next
        
        if tmpNode2 != None:
            head2.next = None
            preNode.next = tmpNode2

        return head1


if __name__ == "__main__":
    head = ListNode(None)
    head.next = ListNode(4)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(1)
    h = Solution().sortList(head)
    while(h!=None):
        print(h.val)
        h = h.next