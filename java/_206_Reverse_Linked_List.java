
class ListNode {
      int val;
      ListNode next;
      ListNode(int x) { val = x; }
 }


public class _206_Reverse_Linked_List {
	public ListNode reverseList(ListNode head) {
		if(head==null)
			return null;
		if(head.next==null)
			return head;
		
		ListNode p,r;
		p=head.next;
		
		head.next=null;
		
		while(p!=null) {
			r=p.next;
			p.next=head.next;
			head.next=p;
			p=r;
		}
		
		ListNode tmp=head;
		
		while(tmp.next!=null)
			tmp=tmp.next;
		
		ListNode newhead=head.next;
		head.next=null;
		tmp.next=head;
		
		return newhead;
    }
}
