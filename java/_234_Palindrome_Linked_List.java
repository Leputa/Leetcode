/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

public class _234_Palindrome_Linked_List {
	 public boolean isPalindrome(ListNode head) {
	        int len=0;
	        ListNode tmp=head;
	        while(tmp!=null) {
	        	tmp=tmp.next;
	        	len++;
	        }
	        if(len==1||len==0)
	        	return true;
	        int mid=0;
	        if(len%2==0)
	        	mid=len/2;
	        else 
	        	mid=len/2+1;
	        tmp=head;
	        for(int i=1;i<mid;i++)
	        	tmp=tmp.next;
	        ListNode midNode=tmp;
	        reverseList(midNode);
	        
	        ListNode tmp1=head;
		    ListNode tmp2=midNode.next;
	        while(tmp2!=null) {
	        	if(tmp1.val!=tmp2.val)
	        		return false;
	        	tmp1=tmp1.next;
	        	tmp2=tmp2.next;
	        }
	        return true;         	
	 }

	private void reverseList(ListNode head) {
		// TODO Auto-generated method stub
		if(head.next==null)
			return;
		ListNode p,r;
		p=head.next;
		head.next=null;
		
		while(p!=null) {
			r=p.next;
			p.next=head.next;
			head.next=p;
			p=r;
		}
	}
}
