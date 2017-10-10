
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

public class _203_Remove_Linked_List_Elements {
	public ListNode removeElements(ListNode head, int val) {
		if(head==null)
			return head;
		ListNode prior=head,tmp=prior.next;
        while(tmp!=null) {
        	if(prior.val==val) {
        		if(prior==head) {
        			head=prior.next;
        			tmp=prior.next;
        		}
        		else {
        			prior.next=null;
            		prior=tmp;
            		tmp=prior.next;
        		}
        	}
        	else if(tmp.val==val) {
        		tmp=tmp.next;
        		prior.next=tmp;
        	}
        	else {
        		tmp=tmp.next;
        		prior=prior.next;
        	}
        }
        if(prior.val==val&&prior==head)
        	return null;
        return head;
    }
}
