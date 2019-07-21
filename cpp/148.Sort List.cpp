
using namespace std;

// Definition for singly-linked list.
 struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
 };

class Solution {
public:
    ListNode* sortList(ListNode* head) {
        if (head == NULL || head->next == NULL)
            return head;
        ListNode *quick_ptr = head;
        ListNode *slow_ptr = head;
        ListNode *preNode;
        while (quick_ptr != NULL && quick_ptr->next != NULL) {
            preNode = slow_ptr;
            slow_ptr = slow_ptr->next;
            quick_ptr = quick_ptr->next->next;
        }
        ListNode *_head = head;
        preNode->next = NULL;
        head = sortList(head);
        slow_ptr = sortList(slow_ptr);
        return merge(head, slow_ptr);
    }

private:
    ListNode* merge(ListNode *head1, ListNode* head2){
        ListNode *tmpNode1 = head1;
        ListNode *tmpNode2 = head2;
        ListNode *head = new ListNode(-1);
        head -> next = head1;
        ListNode *preNode = head;
        while(tmpNode1 != NULL && tmpNode2 != NULL){
            if (tmpNode1->val > tmpNode2->val) {
                ListNode *insertNode = tmpNode2;
                tmpNode2 = tmpNode2->next;
                insertNode->next = tmpNode1;
                preNode->next = insertNode;
                preNode = insertNode;
            }
            else{
                preNode = tmpNode1;
                tmpNode1 = tmpNode1->next;
            }
        }
        if (tmpNode2!=NULL){
            preNode -> next = tmpNode2;
        }
        return head -> next;
    }
};