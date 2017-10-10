/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

public class _83_Remove_Duplicates_from_Sorted_List {

	public ListNode deleteDuplicates(ListNode head) {
		if (head==null)
			return head;
		ListNode tmp=head;
		while(tmp.next!=null) {
			int num=tmp.val;
			ListNode tmp2=tmp.next;
			if(num==tmp2.val) {
				tmp.next=tmp2.next;
				continue;
			}
			tmp=tmp.next;
		}
		return head;
    }
}
