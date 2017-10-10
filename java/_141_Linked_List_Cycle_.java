/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */

public class _141_Linked_List_Cycle_ {
	public boolean hasCycle(ListNode head) {
		if(head==null)
			return false;
		
		if(head.next==null)
			return false;
		if(head.next.next==null)
			return false;
		ListNode ptr1=head.next;
		ListNode ptr2=ptr1.next;

		while(ptr2!=null) {
			if(ptr1==ptr2)
				return true;
			ptr1=ptr1.next;
			if(ptr1==null)
                return false;
            if(ptr2.next==null)
                return false;
            ptr2=ptr2.next.next;
		}
		return false;	
    }
}
